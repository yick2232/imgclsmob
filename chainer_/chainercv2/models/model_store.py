"""
    Model store which provides pretrained models.
"""

__all__ = ['get_model_file']

import os
import zipfile
import logging
import hashlib

_model_sha1 = {name: (error, checksum, repo_release_tag) for name, error, checksum, repo_release_tag in [
    ('alexnet', '1770', '409d189a70b3ca3d2ed25268eb58b37210901719', 'v0.0.394'),
    ('alexnetb', '1858', 'fc907758039a5849093b7d91f22d3ab4e5a80db6', 'v0.0.384'),
    ('zfnet', '1675', '0205a9ab48a3d46407dd6263b1e5e003668ba3e0', 'v0.0.395'),
    ('zfnetb', '1456', '5808c73ebdc868de4da958a3b9b29f9646ecbfbb', 'v0.0.400'),
    ('vgg11', '1017', '7934dcf08eb44f0ebdb0a654733aba0c68e079cd', 'v0.0.381'),
    ('vgg13', '0952', 'f6af5a265c59e6ba07062bd917ef149077019338', 'v0.0.388'),
    ('vgg16', '0833', '5e08a9eccf74f0e89001f2bbccfc3aa2cd4b370f', 'v0.0.401'),
    ('vgg19', '0823', '18980884d7b7e46d0f564548e09af8ea8313789d', 'v0.0.109'),
    ('bn_vgg11', '0937', '8fcdb341a39dd2b45c17d2db5304c61dc1b9227c', 'v0.0.339'),
    ('bn_vgg13', '0887', '1709fd1a05ff302100434574b8c10f9788c06f48', 'v0.0.353'),
    ('bn_vgg16', '0759', '8d6a2a82be26b8126cd8e5ead52c6ba0f2c3bdca', 'v0.0.359'),
    ('bn_vgg19', '0688', '5b6f413cb019374591a6f6597e4ced2ae81fb924', 'v0.0.360'),
    ('bn_vgg11b', '0978', '54b2345ee8b3251a1d9eba3f4b3c7e8b33d0b0ab', 'v0.0.407'),
    ('bn_vgg13b', '1019', '0121b0a47782b5b58c02baa148c88cdc848fc642', 'v0.0.110'),
    ('bn_vgg16b', '0863', 'cbaa2105e000ae844b4775390e9be3b30a23e02e', 'v0.0.110'),
    ('bn_vgg19b', '0816', 'dc5e37a5f6a1d5068b18011ad779062d7b4842cd', 'v0.0.110'),
    ('bninception', '0752', '44a9e12ccd43a521ea09b021214f2951725d0826', 'v0.0.405'),
    ('resnet10', '1389', '66bddf8086630a36f64445dd8fefd895bd9e7189', 'v0.0.248'),
    ('resnet12', '1302', '0cc61e0d7f45d0a58a649850f44fcd0b913ada2a', 'v0.0.253'),
    ('resnet14', '1225', 'b0d4ee074498033f2e0daece5fa4e670f3524bcb', 'v0.0.256'),
    ('resnetbc14b', '1118', 'fad718c2f4b5e74b761564ada9be20062b1a99f1', 'v0.0.309'),
    ('resnet16', '1089', 'ae2206621f7403f55319adeda2c2dfa4cdc8e2e5', 'v0.0.259'),
    ('resnet18_wd4', '1745', '79de61deb25b02203ba3f6da4aaf74a4287fc01d', 'v0.0.262'),
    ('resnet18_wd2', '1285', 'ae41e11d7dec4121f88552b806918bc160fcca05', 'v0.0.263'),
    ('resnet18_w3d4', '1067', '4defa49f9173d881ac7c3f9595db1d176d4be122', 'v0.0.266'),
    ('resnet18', '0959', 'd80fbe604f4d4580f72a523e0577e75b2d4d0661', 'v0.0.153'),
    ('resnet26', '0836', 'ebd61df8afbfcddbc56e169c01fa540081122876', 'v0.0.305'),
    ('resnetbc26b', '0755', '74cf9fe93063636e46bcae0ab00ce02e34be9ae5', 'v0.0.313'),
    ('resnet34', '0746', '1856e049c0f6c18c1812b51e56f7d26efde52733', 'v0.0.291'),
    ('resnetbc38b', '0675', '9210464e98e553bceeb4812d1d72dbeae02eb72a', 'v0.0.328'),
    ('resnet50', '0607', 'f4a162287a4ac0ae502d5de8701fb77bfc958fed', 'v0.0.329'),
    ('resnet50b', '0615', '32bc835e3844b1da62a31198047304b5dc6f799d', 'v0.0.308'),
    ('resnet101', '0601', 'd8cddbea530e052e726d5a1007985beb10ec36eb', 'v0.0.22'),
    ('resnet101b', '0514', '077eb1e282d5ece78d68bb329874b80b8f052e23', 'v0.0.357'),
    ('resnet152', '0535', '64c1daa7752bf9ba8dba6e4e0e4a7947b8c235d9', 'v0.0.144'),
    ('resnet152b', '0483', 'e40bb2226fae35d76342ed943a18c8ff95c4a896', 'v0.0.378'),
    ('preresnet10', '1402', '94e8fc28c7129095273a9e17f6f8d7cc7f88aefc', 'v0.0.249'),
    ('preresnet12', '1318', 'fea1c8c51c1084ff1573abbaea7df6e3aee6a7ee', 'v0.0.257'),
    ('preresnet14', '1224', 'f9973f4f030c379c691ae52d9fe9795595e8e7c6', 'v0.0.260'),
    ('preresnetbc14b', '1153', '1d37e5334d2854dab5b85235fa24c08b6942bbca', 'v0.0.315'),
    ('preresnet16', '1080', 'ac7a346a9f200da344a334848aaf98c984446a29', 'v0.0.261'),
    ('preresnet18_wd4', '1778', '1cf8aa487aa79f903ccd4779d19e3cf01326a937', 'v0.0.272'),
    ('preresnet18_wd2', '1312', 'fa4ce56a87f1763cc037bdf6333d906fbbc86963', 'v0.0.273'),
    ('preresnet18_w3d4', '1069', '25ddcd56602fa811320836d280afa2bd015d7c7f', 'v0.0.274'),
    ('preresnet18', '0954', '21e4811aa9c868bc4afb21ca773493322ba09e82', 'v0.0.140'),
    ('preresnet26', '0838', '8cbc763838f642e8ca770769b57f979745e30be3', 'v0.0.316'),
    ('preresnetbc26b', '0786', '4c1e6a248620c09d884ab7a00a7a9a38b9f36f13', 'v0.0.325'),
    ('preresnet34', '0755', 'b664c649a04a07364543a6125cf1e0286c64af6c', 'v0.0.300'),
    ('preresnetbc38b', '0636', '3105fbe866a6aff33a262efa904f5a2ab01881ff', 'v0.0.348'),
    ('preresnet50', '0624', 'a2bba5b6b4136029626fa717f661495f1e0f0de5', 'v0.0.330'),
    ('preresnet50b', '0634', '605b0eec9ab02677872ebe86acb200c1e7036300', 'v0.0.307'),
    ('preresnet101', '0575', 'f6f6789a895f681be08db6cb9ef184d9009a2f4b', 'v0.0.23'),
    ('preresnet101b', '0538', 'b502bf25880a9579cd22ab89341a6effcf5d48af', 'v0.0.351'),
    ('preresnet152', '0530', '021d99dc3004530a3a1f591e88807ce84e025033', 'v0.0.23'),
    ('preresnet152b', '0500', 'bf54acd9e60bb44be621723bf0c069e2fa6c5d28', 'v0.0.386'),
    ('preresnet200b', '0560', 'f79bd952c08555e0d7bfbcfb2c8214da9c69a0c2', 'v0.0.45'),
    ('preresnet269b', '0558', 'e2e491e1b920d8a063399642a12f7d3e3a695dfb', 'v0.0.239'),
    ('resnext14_16x4d', '1226', '80d9a3310326debcf4f9669842fd03c56d88d504', 'v0.0.370'),
    ('resnext14_32x2d', '1249', '892f96a44bdd01e12eca47d478f3b8c0b3784555', 'v0.0.371'),
    ('resnext14_32x4d', '1115', 'fa0e7f7fd7d4a60a2876bb3c303dd1ee9fea264c', 'v0.0.327'),
    ('resnext26_32x2d', '0849', '58d86996a5e83efe1f49513b7ef5e7803f4830b6', 'v0.0.373'),
    ('resnext26_32x4d', '0719', '62ca50907121ceee5aada95eda7398dca69928cb', 'v0.0.332'),
    ('resnext101_32x4d', '0569', 'c6d1c30dcca4e83c48a2b77cfd36739a0192e244', 'v0.0.26'),
    ('resnext101_64x4d', '0543', 'dd8b7d963c2415ee1207f3705fbc33cb4ba46427', 'v0.0.26'),
    ('seresnet10', '1332', '7943747629e79d58ff4a12b40019de07357a923e', 'v0.0.354'),
    ('seresnet18', '0923', 'b0931abe71a56c02e9c1012d34b99e469602eacc', 'v0.0.355'),
    ('seresnet26', '0806', '00032d5b07f7f580d6b39f433dec3133940d9418', 'v0.0.363'),
    ('seresnetbc26b', '0684', '884c0e6bfaa08ac9250e90716e61e0e491f27648', 'v0.0.366'),
    ('seresnetbc38b', '0579', '7f103cd01544f11e9cd18e9cfefb56b00d215901', 'v0.0.374'),
    ('seresnet50', '0641', 'f3d68cfc8423b786c53390313cabfe0c4410f2d7', 'v0.0.24'),
    ('seresnet50b', '0530', '1ac3bf504713faa817e7cf1c5e8e37fb4368a883', 'v0.0.387'),
    ('seresnet101', '0588', 'e45a9f8f09f1a7439e66032a0d79d7d5a20783b6', 'v0.0.24'),
    ('seresnet152', '0577', 'a089ba52930e9949313b9fba00a1b2e6e68f6ea4', 'v0.0.24'),
    ('sepreresnet10', '1311', '5e38607cfb4971dbd01d6b98058975bbeb6ff61a', 'v0.0.377'),
    ('sepreresnet18', '0939', 'a78ded77bd89ce527d606ebaffb75f0cd2258b2e', 'v0.0.380'),
    ('sepreresnetbc26b', '0638', 'e8393574e457106c4963f7979d91b67dc7554239', 'v0.0.399'),
    ('sepreresnetbc38b', '0566', '4b9ce0969cc05e5a710fed7073132ad025789091', 'v0.0.409'),
    ('seresnext50_32x4d', '0558', '5c435c1b730a0cea61b9657c8796f3c6b95ce9e8', 'v0.0.27'),
    ('seresnext101_32x4d', '0501', '98ea6fc4d36e742a01a0256707a5fa118be166dd', 'v0.0.27'),
    ('senet16', '0807', 'f45aa3fffb8ea5148c53d031e50a3f93ab00ede0', 'v0.0.341'),
    ('senet28', '0591', '7e7bf250ab1bb4842f6dd32ceb93967a7c02239b', 'v0.0.356'),
    ('senet154', '0463', '381d2494a2ad725f62325188f94cd91c795c9902', 'v0.0.28'),
    ('airnet50_1x64d_r2', '0620', 'b6a9359d735916ff8f6192c631b7c646f489fc41', 'v0.0.120'),
    ('airnet50_1x64d_r16', '0650', '95da530f61ae4b0dda4b52c88f37bbc7cc674a03', 'v0.0.120'),
    ('airnext50_32x4d_r2', '0573', '160860f7a1750d759c36e6000080c839cda7ac56', 'v0.0.120'),
    ('bam_resnet50', '0697', 'a8c65533b4fd5e2ebf20c61d5d56936a9e1032b5', 'v0.0.124'),
    ('cbam_resnet50', '0640', 'b2314d9778b321fad2ecf3b350969038236deb96', 'v0.0.125'),
    ('pyramidnet101_a360', '0649', 'b68c786b43512e4297ce00756bd32f8beaa418ba', 'v0.0.104'),
    ('diracnet18v2', '1113', 'b85b43d13697dfbddbea6e46dea4766359fff7e5', 'v0.0.111'),
    ('diracnet34v2', '0948', '0245163a5c947bd6e07a743f17e6ca92c79c84da', 'v0.0.111'),
    ('densenet121', '0683', '4caa2458d39ef6dc467ef3d1a2921ce214b9ddda', 'v0.0.314'),
    ('densenet161', '0620', '6d05f3b9991bc570cb35fff22410d2065b667835', 'v0.0.29'),
    ('densenet169', '0609', '99c9bddf1ae3472efad2b4775fd91b540078e1d3', 'v0.0.406'),
    ('densenet201', '0629', '7770293931c03c2852115267dde3100d7140bbba', 'v0.0.29'),
    ('condensenet74_c4_g4', '0861', 'ef6077ec5348504346b3bcbaacbc308f825a9f87', 'v0.0.36'),
    ('condensenet74_c8_g8', '1043', '277fbfb898e0c8c7de8475184bcf5e651da10acc', 'v0.0.36'),
    ('peleenet', '1127', 'ef057fc99fda7df002d9654f0a74452e4b4b75d0', 'v0.0.141'),
    ('wrn50_2', '0613', 'd0cd9171917f04095ba8f4f48413a2ddd1ee5bc2', 'v0.0.113'),
    ('drnc26', '0788', '762c34c1f20d8ad76cec251cc0125936b608a3bc', 'v0.0.116'),
    ('drnc42', '0693', 'ec938cc429d3d0e54c34243c10be83ffae38023e', 'v0.0.116'),
    ('drnc58', '0629', '063ef19974f0158bcc6b9e4020729291462a08a3', 'v0.0.116'),
    ('drnd22', '0850', 'b25d475756dcfceb1321190b9cca6cc1f7e8e55a', 'v0.0.116'),
    ('drnd38', '0736', '153481d6f8d0b113981fc323f5b2c2ad6b2ad7f5', 'v0.0.116'),
    ('drnd54', '0623', '31e8eeb88bdbb07d8613a16471c8c5bd67ae823a', 'v0.0.116'),
    ('drnd105', '0584', 'c0d7657b2d3c4cf7d97ff407cd50dda5d1bd1880', 'v0.0.116'),
    ('dpn68', '0656', 'bf9b72e9749da4c6ee5a544639f78ac7fa85f7ce', 'v0.0.310'),
    ('dpn98', '0553', '9cd5733573f7a99062d16cd8850bb82d684704bb', 'v0.0.34'),
    ('dpn131', '0523', 'e37215991fa7e9f49245843d53de63ef1717f293', 'v0.0.34'),
    ('darknet_tiny', '1746', 'b04fa46318a78e977aa5a117786968d98d325871', 'v0.0.69'),
    ('darknet_ref', '1671', 'b2d5721f3a5f6f05cc785d57ff7a63fe82f6325e', 'v0.0.64'),
    ('darknet53', '0556', '42c57951fc2668c1a81ede52e6f4de4aac7e0278', 'v0.0.150'),
    ('irevnet301', '0887', 'ed6e6df033e659893b9021a6381f101feff002b8', 'v0.0.251'),
    ('bagnet9', '3545', '8ac8c0f7ed5d64aa54d628f434f1e60b0e22bff0', 'v0.0.255'),
    ('bagnet17', '2151', '571889691e8dfedac68e9b6226a9d4a2b237594c', 'v0.0.255'),
    ('bagnet33', '1492', 'a7be162cc1572d5d32f30643ddcd2ead5834cb17', 'v0.0.255'),
    ('dla34', '0823', '45504b0927fab7165e863c6801f9c0f10a906731', 'v0.0.202'),
    ('dla46c', '1292', '98e3efd5e9cd50d3b403bc36b71614aad4bf69ff', 'v0.0.282'),
    ('dla46xc', '1228', 'c2dc61bc0ac57dc4f5b4041d3261ac3d7df521b2', 'v0.0.293'),
    ('dla60', '0711', '92693875e59ad39963ecd641cef34c0d4b24d02e', 'v0.0.202'),
    ('dla60x', '0620', '444f31ea8f3f17128eae5359c38e874d171c3e60', 'v0.0.202'),
    ('dla60xc', '1076', '4c418399df58871201cc0487db4e72411ff53c44', 'v0.0.289'),
    ('dla102', '0642', 'c4ee6dcb1261ad2e4b69a906877d3cb024197307', 'v0.0.202'),
    ('dla102x', '0599', '7f83bc042bb9ae6f8443d73cacc685f5bc8714b5', 'v0.0.202'),
    ('dla102x2', '0554', '6a27a09408abaffb55ed8a041f0390c47631d522', 'v0.0.202'),
    ('dla169', '0590', '96b692a8f94c2135d5d7fc5eba6b3605c5e0595e', 'v0.0.202'),
    ('fishnet150', '0639', '114d15a6db53a9712a17afdb2a3fba4cdc3250f5', 'v0.0.168'),
    ('espnetv2_wd2', '2108', '72efda3a821eb165b2cccf34532d3c26d6525bb7', 'v0.0.238'),
    ('espnetv2_w1', '1431', 'eab8d605b475bd3659d6834ba5140d327f57c7de', 'v0.0.238'),
    ('espnetv2_w5d4', '1268', 'dc69f420f422154ab7242bcd95488541491d4982', 'v0.0.238'),
    ('espnetv2_w3d2', '1192', '2b7fc5cfacc15a63ec60109bb1b8c48d09df2a7e', 'v0.0.238'),
    ('espnetv2_w2', '0990', 'bfb3ab7c84239ff53003865e456c2a0178c48f12', 'v0.0.238'),
    ('squeezenet_v1_0', '1738', '4c55a6a5c7ae14b88a7989eea5a7dc60960120ef', 'v0.0.128'),
    ('squeezenet_v1_1', '1740', 'b236c2047fe1d9b283ccfaabb763143a214ecc33', 'v0.0.88'),
    ('squeezeresnet_v1_0', '1766', '6dc69dc26e83beaa98fa77ee64d208294f7850f9', 'v0.0.178'),
    ('squeezeresnet_v1_1', '1787', 'f40e60512a8b66f314f4d7ffab9b18dd31715b3a', 'v0.0.70'),
    ('sqnxt23_w1', '1903', 'ef3d725b418277e98ed5e590e615cc13df2f001e', 'v0.0.171'),
    ('sqnxt23v5_w1', '1786', '8b24c6e36f00be6d1b970f3c10e2b956fe281357', 'v0.0.172'),
    ('sqnxt23_w3d2', '1344', 'a5c3b21eb05532cba4b35f530fea2bdaac3d6bf5', 'v0.0.210'),
    ('sqnxt23v5_w3d2', '1292', 'c997e27957a32f89538f23d86207a044d2dc0c93', 'v0.0.212'),
    ('sqnxt23_w2', '1082', 'cf7aebefd6abb1fb3fea72dc10e0ad3dd145be8b', 'v0.0.240'),
    ('sqnxt23v5_w2', '1043', 'e9e849cdfeba0f8b3cdfd34bc214cc6526016dc4', 'v0.0.216'),
    ('shufflenet_g1_wd4', '3681', '15d3e7871b85cee9283663bbbc78dfe5e1a1a1db', 'v0.0.134'),
    ('shufflenet_g3_wd4', '3616', '064f7f7f1dd327f43e16adf5e4864a31e16d9ad9', 'v0.0.135'),
    ('shufflenet_g1_wd2', '2235', '5d83cc2822fbd0669af75d93c7940aa09e78d317', 'v0.0.174'),
    ('shufflenet_g3_wd2', '2061', '557e4397da6cebf2dd7b70e8039100f07414437a', 'v0.0.167'),
    ('shufflenet_g1_w3d4', '1677', 'b5515ea9c945c92fc4272ba7daf0002314cc61de', 'v0.0.218'),
    ('shufflenet_g3_w3d4', '1613', '55129cb578d0d53bb962e703da0746930d092c2a', 'v0.0.219'),
    ('shufflenet_g1_w1', '1348', '37cc6c5f70ad982ff3fc9c92a0ae6405bb46e2c7', 'v0.0.223'),
    ('shufflenet_g2_w1', '1333', 'e473c62fe289cc2563cb17cfa4c8562f25fd6e49', 'v0.0.241'),
    ('shufflenet_g3_w1', '1326', '95df048749f08aa69e9aed33a8bd7182b4caf2df', 'v0.0.244'),
    ('shufflenet_g4_w1', '1308', '8ed92f35a9d69874e3c9d040785f6c71c54d976c', 'v0.0.245'),
    ('shufflenet_g8_w1', '1321', '2fea8945a2115c718cdb09a22a95f4e2808e098b', 'v0.0.250'),
    ('shufflenetv2_wd2', '2073', 'c5e5a23c300c800d55e2f45e1dcb2e12907c0eae', 'v0.0.90'),
    ('shufflenetv2_w1', '1298', '3830a2da0701f2b31385aceeb828101008446812', 'v0.0.133'),
    ('shufflenetv2_w3d2', '1014', '5f75edb160035ea6e8f2896e4c233fa2a1494af1', 'v0.0.288'),
    ('shufflenetv2_w2', '0899', 'a44b1d5d86f6041e8d34fb3b13563d144dc6b4c0', 'v0.0.301'),
    ('shufflenetv2b_wd2', '1787', '08a12021fa41000f5f6206446d34daa2eebb8d00', 'v0.0.157'),
    ('shufflenetv2b_w1', '1100', '21562fb22a353559c6c732e54e807766bb576dee', 'v0.0.161'),
    ('shufflenetv2b_w3d2', '0878', '7a5c7ed4aa440788875680b2a12531716ee02f98', 'v0.0.203'),
    ('shufflenetv2b_w2', '0810', '636e281ce91bf852fd20adb07f0037be8dd3d6b6', 'v0.0.242'),
    ('menet108_8x1_g3', '2042', '9e3ff283ac81b4f4e6d4a5b11d8d54b63f4aa2f0', 'v0.0.89'),
    ('menet128_8x1_g4', '1919', 'f6fd56fae09d0c528c902d1381f7cf401590d130', 'v0.0.103'),
    ('menet160_8x1_g8', '2042', '250fd7654d54c79477ef7cbf402e15d69ea3ea6a', 'v0.0.154'),
    ('menet228_12x1_g3', '1301', '39c25ca345751cac91395a602565796393fea60d', 'v0.0.131'),
    ('menet256_12x1_g4', '1218', '57160b09127535a3733f22af10d50fb16d5d2643', 'v0.0.152'),
    ('menet348_12x1_g3', '0936', 'ee7e056d0f38a68a6d6c85fe8162bee944a73121', 'v0.0.173'),
    ('menet352_12x1_g8', '1172', 'c256ae25591e33ce6b9e12177305eacb3dd9620c', 'v0.0.198'),
    ('menet456_24x1_g3', '0779', '5af355f6457347168d5b95323b6d7480360398d8', 'v0.0.237'),
    ('mobilenet_wd4', '2216', '09c50ab8d72049a4aa9cae4bd1502859522b9a70', 'v0.0.62'),
    ('mobilenet_wd2', '1337', '48d12ee398fa6dc23596f669fb202f08108a6ccc', 'v0.0.156'),
    ('mobilenet_w3d4', '1053', 'd7ec3192f88b7017d477fdb704ad6ad77a4c5cc1', 'v0.0.130'),
    ('mobilenet_w1', '0866', 'b888f817a2978cdeb00a09fd5e71c3f2a52ddd8c', 'v0.0.155'),
    ('fdmobilenet_wd4', '3063', '55407f3a3e3370fa2951f651f14faac3bf9a9f28', 'v0.0.177'),
    ('fdmobilenet_wd2', '1976', '6299d44272390440be808e58059219b0d57907e4', 'v0.0.83'),
    ('fdmobilenet_w3d4', '1599', 'cdfc2e043017be0166cf06cb9f49e0f516aa5d15', 'v0.0.159'),
    ('fdmobilenet_w1', '1316', '0ed6f00cbb5095eff002882e31c006edb1c5235e', 'v0.0.162'),
    ('mobilenetv2_wd4', '2411', '9fc398d348226c410659464d12b0fe6b7d4506e7', 'v0.0.137'),
    ('mobilenetv2_wd2', '1444', 'ca0906e176f15855aa8c8d771c841c3f9cd3d454', 'v0.0.170'),
    ('mobilenetv2_w3d4', '1047', 'a25fd26c426b5af8c5761b9d634b508622f019cf', 'v0.0.230'),
    ('mobilenetv2_w1', '0866', 'efc3331e08dfc578526bbf5e161c15e50b146c63', 'v0.0.213'),
    ('mobilenetv3_large_w1', '0771', 'b78635d1203847115abdcf476cc8bd91d6e4aa7e', 'v0.0.411'),
    ('igcv3_wd4', '2828', '25942192926a7dcdd0c57238336a8a0ef840e079', 'v0.0.142'),
    ('igcv3_wd2', '1704', '86246558ade35232344a4c448288ae3927143f9c', 'v0.0.132'),
    ('igcv3_w3d4', '1099', 'b0dbc54a5c40c7bd55ebd3cab05e39263064f4ec', 'v0.0.207'),
    ('igcv3_w1', '0898', '5fd85acd8a4ed75845e2ef770c25460c5f7eff95', 'v0.0.243'),
    ('mnasnet', '1144', '688e523d02834b34f4a693a1b18e7a523483eb58', 'v0.0.117'),
    ('darts', '0897', '8986fe64b3f853704a88010f0a735a9e6e33bd97', 'v0.0.118'),
    ('proxylessnas_cpu', '0752', '22bd211b1fbf219f1cb28ed7a407e3949a2037ea', 'v0.0.324'),
    ('proxylessnas_gpu', '0723', 'b81256a146f7e0c08a5d5004332bb409576799f3', 'v0.0.333'),
    ('proxylessnas_mobile', '0785', '561f3416638764215dcd975b2f7e27fc34974929', 'v0.0.326'),
    ('proxylessnas_mobile14', '0651', '7467ce2d73d14facfc593c395fe73a6f2d7dc456', 'v0.0.331'),
    ('fbnet_cb', '0784', 'ef40d7858dbfe46a8390829c364528549b4aa870', 'v0.0.415'),
    ('xception', '0547', '7a5be9582fd7a4771ede5290645be394d66d29ca', 'v0.0.115'),
    ('inceptionv3', '0561', '4ddea4df44f132ffc9e2b22b1e7d686f8b59703b', 'v0.0.92'),
    ('inceptionv4', '0526', '02e53701d1bda64b057b41fa90d8e04a17d07f66', 'v0.0.105'),
    ('inceptionresnetv2', '0492', '3d3de82bb9db27b260603fe2f956ad929c3eb277', 'v0.0.107'),
    ('polynet', '0450', '6dc7028b0edc48c452f83dd38448b1242c554a5e', 'v0.0.96'),
    ('nasnet_4a1056', '0796', 'f09950c0f4a333007dc33049531534b8cd9f8521', 'v0.0.97'),
    ('nasnet_6a4032', '0422', 'd49d46631abda0ec7ac4a0076e6f8d05bf99b7d1', 'v0.0.101'),
    ('pnasnet5large', '0426', '3c2755dce80a29dea19b398dce514a640da2aaa3', 'v0.0.114'),
    ('spnasnet', '0869', '064ffaa7c8062fe1cf7b01bc365d406d4f780ef8', 'v0.0.416'),
    ('efficientnet_b0', '0725', '8d6f17447e9fa2da26963b72cf8fd359aebba504', 'v0.0.364'),
    ('efficientnet_b1', '0633', '4ac377d926a55be53052c42f21678c26862a81eb', 'v0.0.376'),
    ('efficientnet_b0b', '0669', '366e9c540a59d954fdfd13b46f47b91231aa8700', 'v0.0.403'),
    ('efficientnet_b1b', '0567', '2826a68613cbecc782819f24ddd5b031bfed1586', 'v0.0.403'),
    ('efficientnet_b2b', '0514', '93c91747fda8ea4f20d6eacb678ba13bacb455bc', 'v0.0.403'),
    ('efficientnet_b3b', '0436', '82eb9d9104377ec90cfecc8e8f04a9876d3c16f9', 'v0.0.403'),
    ('efficientnet_b4b', '0392', '81138451fda7683c964ea52a9f2a7ea48622ef33', 'v0.0.403'),
    ('efficientnet_b5b', '0339', 'fb684f5dc219d9463acb5aa42b48bd920f887cd1', 'v0.0.403'),
    ('efficientnet_b6b', '0324', 'acaad4db1bb064f088d53b620ee682ecc328c80d', 'v0.0.403'),
    ('efficientnet_b7b', '0323', '031b7bd5e4c361f734eb40bba1e10a11df0a8374', 'v0.0.403'),
    ('mixnet_s', '0728', 'dc6c60c8cfac2e7a90ae68a76ed4fda17b44cf7a', 'v0.0.412'),
    ('mixnet_m', '0675', '4979acf0bd7ddef39f30f80ae296d480e5120609', 'v0.0.413'),
    ('mixnet_l', '0590', 'f942b4c57f08316283841a18ae2bd8fe4a9b1b1a', 'v0.0.414'),
    ('resnetd50b', '0550', '7ba88f0436b3fa598520424bb463ac985ffb0caf', 'v0.0.296'),
    ('resnetd101b', '0460', 'b90f971e4514345fb885de95165ddcc4e6610234', 'v0.0.296'),
    ('resnetd152b', '0470', '41442334cde93c9744d2a86288d11614c848503a', 'v0.0.296'),
    ('nin_cifar10', '0743', '045abfde63c6b73fbb1b6c6b062c9da5e2485750', 'v0.0.175'),
    ('nin_cifar100', '2839', '891047637c63f274d4138a430fcaf5f92f054ad4', 'v0.0.183'),
    ('nin_svhn', '0376', '2fbe48d0dd165c97acb93cf0edcf4b847651e3a0', 'v0.0.270'),
    ('resnet20_cifar10', '0597', '15145d2e00c85b5c295b6999068ce4b494febfb0', 'v0.0.163'),
    ('resnet20_cifar100', '2964', '6a85f07e9bda4721ee68f9b7350250b866247324', 'v0.0.180'),
    ('resnet20_svhn', '0343', 'b6c1dc9982e1ee04f089ca02d5a3dbe549b18c02', 'v0.0.265'),
    ('resnet56_cifar10', '0452', 'eb7923aa7d53e4e9951483b05c9629010fbd75a4', 'v0.0.163'),
    ('resnet56_cifar100', '2488', '2d641cdef73a9cdc440d7ebfb665167907a6b3bd', 'v0.0.181'),
    ('resnet56_svhn', '0275', 'cf18a0720e4e73e5d36832e24a36b78351f9c266', 'v0.0.265'),
    ('resnet110_cifar10', '0369', '27d76fce060ce5737314f491211734bd10c60308', 'v0.0.163'),
    ('resnet110_cifar100', '2280', 'd2ec4ff1c85095343031a0b11a671c4799ae1187', 'v0.0.190'),
    ('resnet110_svhn', '0245', 'f274056a4f3b187618ab826aa6e3ade028a3a4da', 'v0.0.265'),
    ('resnet164bn_cifar10', '0368', 'd86593667f30bfef0c0ad237f2da32601b048312', 'v0.0.179'),
    ('resnet164bn_cifar100', '2044', '190ab6b485404e43c41a85542e57adb051744aa0', 'v0.0.182'),
    ('resnet164bn_svhn', '0242', 'b4c1c66ccc47f0802058fcd469844811f214bbca', 'v0.0.267'),
    ('resnet272bn_cifar10', '0333', 'b7c6902a5e742b2c46c9454be5962f9a5e5a0fa5', 'v0.0.368'),
    ('resnet272bn_cifar100', '2007', 'fe6b27f8b18785d568719dfbaea79ae05eb0aefe', 'v0.0.368'),
    ('resnet272bn_svhn', '0243', '693d5c393d2823146a1bdde0f8b11bb21ccd8c12', 'v0.0.368'),
    ('resnet542bn_cifar10', '0343', 'b6598e7a0e5bd800b4425424b43274a96677e77b', 'v0.0.369'),
    ('resnet542bn_cifar100', '1932', '4f95b380a755ae548187bfa0da038565c50e1e26', 'v0.0.369'),
    ('resnet542bn_svhn', '0234', '7421964d2246a7b5ba7f9baf294cc3bd06329ad8', 'v0.0.369'),
    ('resnet1001_cifar10', '0328', '0e27556cdc97b7d0612d4518546a9b0479e030c3', 'v0.0.201'),
    ('resnet1001_cifar100', '1979', '6416c8d2f86debf42f1a3798e4b53fa8d94b0347', 'v0.0.254'),
    ('resnet1001_svhn', '0241', 'c8b23d4c50359cac2fbd837ed754cc4ea7b3b060', 'v0.0.408'),
    ('resnet1202_cifar10', '0353', 'd82bb4359d16e68989547f8b1153c8f23264e46c', 'v0.0.214'),
    ('resnet1202_cifar100', '2156', '711136021e134b4180cc49c7bb1dda2bd0d4ab49', 'v0.0.410'),
    ('preresnet20_cifar10', '0651', '5cf94722c7969e136e2174959fee4d7b95528f54', 'v0.0.164'),
    ('preresnet20_cifar100', '3022', 'e3fd9391a621da1afd77f1c09ae0c9bdda4e17aa', 'v0.0.187'),
    ('preresnet20_svhn', '0322', '8e56898f75a9ba2c016b1e14e880305e55a96ea7', 'v0.0.269'),
    ('preresnet56_cifar10', '0449', '73ea193a6f184d034a4b5b911fe6d23473eb0220', 'v0.0.164'),
    ('preresnet56_cifar100', '2505', 'f879fb4e9c9bc328b97ca8999575ea29343bbd79', 'v0.0.188'),
    ('preresnet56_svhn', '0280', 'f512407305efa862c899a56cfc86003ee9ca0e9f', 'v0.0.269'),
    ('preresnet110_cifar10', '0386', '544ed0f0e0b3c0da72395924e2ea381dbf381e52', 'v0.0.164'),
    ('preresnet110_cifar100', '2267', '4e010af04fefb74f6535a1de150f695460ec0550', 'v0.0.191'),
    ('preresnet110_svhn', '0279', '8dcd3ae54540a62f6a9b87332f0aa2abfc587600', 'v0.0.269'),
    ('preresnet164bn_cifar10', '0364', 'c0ff243801f078c6e6be72e1d3b67d88d61c4454', 'v0.0.196'),
    ('preresnet164bn_cifar100', '2018', '5228dfbdebf0f4699dae38a4a9b8310b08189d48', 'v0.0.192'),
    ('preresnet164bn_svhn', '0258', '69de71f53eee796710e11dae53f10ed276588df0', 'v0.0.269'),
    ('preresnet272bn_cifar10', '0325', '8f8f375dfca98fb0572b2de63ca3441888c52a88', 'v0.0.389'),
    ('preresnet272bn_cifar100', '1963', '52a0ebabfa75366e249e612b9556c87618acf41e', 'v0.0.389'),
    ('preresnet272bn_svhn', '0234', 'b2cc8842932feb8f04547d5341f00ef2a3846d8a', 'v0.0.389'),
    ('preresnet542bn_cifar10', '0314', '86a2b5f51c4e8064ba3093472a65e52e4d65f6be', 'v0.0.391'),
    ('preresnet542bn_cifar100', '1871', 'd7343a662a78d29fe14f98e7dba6d79096f43904', 'v0.0.391'),
    ('preresnet542bn_svhn', '0236', '67f372d8a906e75f2aa3a32396e757851fd6e1fd', 'v0.0.391'),
    ('preresnet1001_cifar10', '0265', '1f3028bdf7143b8f99340b1b1a0a8e029d7020a0', 'v0.0.209'),
    ('preresnet1001_cifar100', '1841', 'fcbddbdb462da0d77c50026878ea2cfb6a95f5d4', 'v0.0.283'),
    ('preresnet1202_cifar10', '0339', 'cc2bd85a97842f7a444deb78262886a264a42c25', 'v0.0.246'),
    ('resnext29_32x4d_cifar10', '0315', '442eca6c30448563f931174d37796c2f08c778b7', 'v0.0.169'),
    ('resnext29_32x4d_cifar100', '1950', 'de139852f2876a04c74c271d50f0a50ba75ece3e', 'v0.0.200'),
    ('resnext29_32x4d_svhn', '0280', '0a402faba812ae0b1238a6da95adc734a5a24f16', 'v0.0.275'),
    ('resnext29_16x64d_cifar10', '0241', 'e80d3cb5f8d32be2025fe8fb7a7369b2d004217e', 'v0.0.176'),
    ('resnext29_16x64d_cifar100', '1693', '762f79b3506528f817882c3a47252c2f42e9376b', 'v0.0.322'),
    ('resnext29_16x64d_svhn', '0268', '04ffa5396ae4a61e60a30f86cd5180611ce94772', 'v0.0.358'),
    ('resnext272_1x64d_cifar10', '0255', '1ca6630049e54d9d17887c0af26ab6f848d30067', 'v0.0.372'),
    ('resnext272_1x64d_cifar100', '1911', '9a9b397c1091c6bd5b0f4b13fb6567a99d7aa7ac', 'v0.0.372'),
    ('resnext272_1x64d_svhn', '0235', 'b12f9d9ce073c72c2e5509a27a5dd065a7b5d05f', 'v0.0.372'),
    ('resnext272_2x32d_cifar10', '0274', '94e492a4391e589e6722a91ddc8b18df4dc89ed0', 'v0.0.375'),
    ('resnext272_2x32d_cifar100', '1834', 'bbc0c87cad70745f2aa86241521449ab7f9fd3bf', 'v0.0.375'),
    ('resnext272_2x32d_svhn', '0244', 'd9432f639120985968afc9b1bdde666ceaad53c9', 'v0.0.375'),
    ('seresnet20_cifar10', '0601', '143eba2ad59cc9f7e539d97445eb4fe13aad1a6e', 'v0.0.362'),
    ('seresnet20_cifar100', '2854', '1240e42f79500ddca2e471f543ff1aa28f20af16', 'v0.0.362'),
    ('seresnet20_svhn', '0323', '6c611f0a860d7a0c161602bfc268ccb8563376ee', 'v0.0.362'),
    ('seresnet56_cifar10', '0413', '66486cdbab43e244883ca8f26aa93da2297f9468', 'v0.0.362'),
    ('seresnet56_cifar100', '2294', 'ab7e54434bdee090f0694d3ba96122c441b7753b', 'v0.0.362'),
    ('seresnet56_svhn', '0264', '0a017d76364bb219b35aa2a792291acb1554e251', 'v0.0.362'),
    ('seresnet110_cifar10', '0363', '9a85ff9521387e1155437e691d5ccb411b28e441', 'v0.0.362'),
    ('seresnet110_cifar100', '2086', '298d298ea6747ff9f9277be08838f723c239e4e3', 'v0.0.362'),
    ('seresnet110_svhn', '0235', '525399af7c6f717aabc6c1c024c863191a1a28d9', 'v0.0.362'),
    ('seresnet164bn_cifar10', '0339', '4c59e76fc3264532142b37db049d3ff422b6d5f4', 'v0.0.362'),
    ('seresnet164bn_cifar100', '1995', 'cdac82fd3133bfd4d8cd261016a68fe95928ea4b', 'v0.0.362'),
    ('seresnet164bn_svhn', '0245', '31e8d2beeeb74a444ff756cafc7f1b557009cddc', 'v0.0.362'),
    ('seresnet272bn_cifar10', '0339', '8081d1be9a5eb985c828b6f60e41b3d689c84659', 'v0.0.390'),
    ('seresnet272bn_cifar100', '1907', 'a83ac8d69535cfb394be7e790ff9683d65e2b3f9', 'v0.0.390'),
    ('seresnet272bn_svhn', '0238', '2b28cd779296d2afbb789cee7b73a80b4b07e4a9', 'v0.0.390'),
    ('seresnet542bn_cifar10', '0347', 'e67d0c059a4f5c2e97790eb50d03013430f5a2fd', 'v0.0.385'),
    ('seresnet542bn_cifar100', '1887', 'dac530d68dff49ec37756212d3f9b52c256448fb', 'v0.0.385'),
    ('seresnet542bn_svhn', '0226', '9571b88bd6ac07407a453651feb29b376609933c', 'v0.0.385'),
    ('sepreresnet20_cifar10', '0618', 'cbc1c4df6061046a7cf99e5739a5c5df811da420', 'v0.0.379'),
    ('sepreresnet20_cifar100', '2831', 'e54804186c83656f8d9705ff021fd83772a0c6eb', 'v0.0.379'),
    ('sepreresnet20_svhn', '0324', '04dafec1e0490ecc7001a0ca9547b60ba6314956', 'v0.0.379'),
    ('sepreresnet56_cifar10', '0451', '0b34942c73cd2d196aa01763fb5167cb78f2b56d', 'v0.0.379'),
    ('sepreresnet56_cifar100', '2305', '1138b50001119765d50eeaf10a3fca15ccf6040a', 'v0.0.379'),
    ('sepreresnet56_svhn', '0271', '150740af292a0c5c8a6d499dfa13b2a2c5672e60', 'v0.0.379'),
    ('sepreresnet110_cifar10', '0454', '4c062f46d2ec615cbfc0e07af12febcddcd16364', 'v0.0.379'),
    ('sepreresnet110_cifar100', '2261', 'b525d8b1568e1cad021026930f5b5283bdba8b49', 'v0.0.379'),
    ('sepreresnet110_svhn', '0259', 'eec4c9f3c94cad32557f0a969a8ec1d127877ab6', 'v0.0.379'),
    ('sepreresnet164bn_cifar10', '0373', 'e82ad7ffc78c00ad128ab4116dbd3f3eae028c19', 'v0.0.379'),
    ('sepreresnet164bn_cifar100', '2005', 'baf00211c3da54ddf50000629b8419da8af599d8', 'v0.0.379'),
    ('sepreresnet164bn_svhn', '0256', '36362d66943c89b7b7153eeaf0cfc2113369b6d5', 'v0.0.379'),
    ('sepreresnet272bn_cifar10', '0339', '02e141138736d647bcbdb4f0fc0d81a7bc8bef85', 'v0.0.379'),
    ('sepreresnet272bn_cifar100', '1913', 'd37b7af28056f42bbd11df19479cbdb0b0ac7f63', 'v0.0.379'),
    ('sepreresnet272bn_svhn', '0249', '44b18f81ea4ba5ec6a7ea725fc9c0798a670c161', 'v0.0.379'),
    ('sepreresnet542bn_cifar10', '0308', '1e726874123afc10d24cf58779347b13fdfa3b00', 'v0.0.382'),
    ('sepreresnet542bn_cifar100', '1945', 'aadac5fbe15f5227ff02cdf9abf3c2f27b602db4', 'v0.0.382'),
    ('sepreresnet542bn_svhn', '0247', 'ff5682df9a051821a4fda0a1f1fe81dbf96da479', 'v0.0.382'),
    ('pyramidnet110_a48_cifar10', '0372', '965fce37e26ef4e3724df869fe90283669fe9daf', 'v0.0.184'),
    ('pyramidnet110_a48_cifar100', '2095', 'b74f12c8d11de3ddd9fa51fe93c1903675a43a3c', 'v0.0.186'),
    ('pyramidnet110_a48_svhn', '0247', 'e750bd672b24bb60eca0527fd11f9866a9fc8329', 'v0.0.281'),
    ('pyramidnet110_a84_cifar10', '0298', '7b38a0f65de0bec2f4ceb83398fef61009a2c129', 'v0.0.185'),
    ('pyramidnet110_a84_cifar100', '1887', '842b3809619ec81c6e27defcad9df5c3dbc0ae55', 'v0.0.199'),
    ('pyramidnet110_a84_svhn', '0243', '56b06d8fd9ec043ccf5acc0b8a129bee2ef9a901', 'v0.0.392'),
    ('pyramidnet110_a270_cifar10', '0251', 'b3456ddd5919ef861ec607f8287bd071de0ba077', 'v0.0.194'),
    ('pyramidnet110_a270_cifar100', '1710', '56ae71355de25daafe34c51b91fe5b4bdab1f6ac', 'v0.0.319'),
    ('pyramidnet110_a270_svhn', '0238', 'fdf9f2da74bae9d4280f329554a12c9770fde52f', 'v0.0.393'),
    ('pyramidnet164_a270_bn_cifar10', '0242', '783e21b5856a46ee0087535776703eb7ca0c24ae', 'v0.0.264'),
    ('pyramidnet164_a270_bn_cifar100', '1670', '7614c56c52d9a6ca42d0446ab7b5c9a5e4eae63f', 'v0.0.312'),
    ('pyramidnet164_a270_bn_svhn', '0233', '6dcd188245b4c4edc8a1c751cd54211d26e2c603', 'v0.0.396'),
    ('pyramidnet200_a240_bn_cifar10', '0244', '89ae1856e23a67aac329df11775346e6bf8e00b7', 'v0.0.268'),
    ('pyramidnet200_a240_bn_cifar100', '1609', '0729db3729da20627c7e91bd1e9beff251f2b82c', 'v0.0.317'),
    ('pyramidnet200_a240_bn_svhn', '0232', 'b5876d02190e3e6a7dc7c0cd6e931e96151c34e9', 'v0.0.397'),
    ('pyramidnet236_a220_bn_cifar10', '0247', '6b9a29664f54d8ea82afc863670a79099e6f570a', 'v0.0.285'),
    ('pyramidnet236_a220_bn_cifar100', '1634', 'fd14728bc8ca8ccb205880d24d38740dad232d00', 'v0.0.312'),
    ('pyramidnet236_a220_bn_svhn', '0235', 'bb39a3c6f8ee25c32a40304ebf266a9521b513c4', 'v0.0.398'),
    ('pyramidnet272_a200_bn_cifar10', '0239', '533f8d89abe57656e1baef549dabedbc4dcefbe8', 'v0.0.284'),
    ('pyramidnet272_a200_bn_cifar100', '1619', '4ba0ea07d5f519878d33f7b3741f742ae12fef50', 'v0.0.312'),
    ('pyramidnet272_a200_bn_svhn', '0240', '2ace26878c803cc3a415d8f897bf9d3ec7f4d19c', 'v0.0.404'),
    ('densenet40_k12_cifar10', '0561', 'a37df881a11487fdde772254a82c20c3e45b461b', 'v0.0.193'),
    ('densenet40_k12_cifar100', '2490', 'd06839db7eec0331354ca31b421c6fbcd4665fd3', 'v0.0.195'),
    ('densenet40_k12_svhn', '0305', '8d563cdf9dcd1d4822669f6119f6e77b4e03c162', 'v0.0.278'),
    ('densenet40_k12_bc_cifar10', '0643', '234918e7144b95454e1417035c73391663a68401', 'v0.0.231'),
    ('densenet40_k12_bc_cifar100', '2841', '968e5667c29dd682a90c3f8a488e00a9efe0d29f', 'v0.0.232'),
    ('densenet40_k12_bc_svhn', '0320', '52bd79007dd8a8b60b9aef94a555161c9faf4b37', 'v0.0.279'),
    ('densenet40_k24_bc_cifar10', '0452', '3ec459af58cf2106bfcbdad090369a1f3d41ef3c', 'v0.0.220'),
    ('densenet40_k24_bc_cifar100', '2267', 'f744296d04d703c202b0b78cdb32e7fc40116584', 'v0.0.221'),
    ('densenet40_k24_bc_svhn', '0290', '268af51aaea47003c9ce128ddb76507dabb0726e', 'v0.0.280'),
    ('densenet40_k36_bc_cifar10', '0404', '6be4225a6d0e5fb68bdc9cda471207c0b5420395', 'v0.0.224'),
    ('densenet40_k36_bc_cifar100', '2050', '49b6695fe06d98cfac5d4fdbdb716edb268712c2', 'v0.0.225'),
    ('densenet40_k36_bc_svhn', '0260', '47ef4d80ef3f541b795a1aee645ff9e8bada6101', 'v0.0.311'),
    ('densenet100_k12_cifar10', '0366', '85031735e1c80d3a6254fe8649c5e9bae2d54315', 'v0.0.205'),
    ('densenet100_k12_cifar100', '1964', 'f04f59203ad863f466c25fa9bbfc18686d72a46a', 'v0.0.206'),
    ('densenet100_k12_svhn', '0260', 'c57bbabec45492bcc4a2587443b06bf400c6ea25', 'v0.0.311'),
    ('densenet100_k24_cifar10', '0313', '939ef3090b6219e5afabc97f03cc34365c729ada', 'v0.0.252'),
    ('densenet100_k24_cifar100', '1808', '47274dd8a35bfeb77e9a077275111e4a94d561e4', 'v0.0.318'),
    ('densenet100_k12_bc_cifar10', '0416', '160a064165eddf492970a99b5a8ca9689bf94fea', 'v0.0.189'),
    ('densenet100_k12_bc_cifar100', '2119', 'a37ebc2a083fbe8e7642988945d1092fb421f182', 'v0.0.208'),
    ('densenet190_k40_bc_cifar10', '0252', '57f2fa706376545c260f4848a1112cd03069a323', 'v0.0.286'),
    ('densenet250_k24_bc_cifar10', '0267', '03b268872cdedadc7196783664b4d6e72b00ecd2', 'v0.0.290'),
    ('densenet250_k24_bc_cifar100', '1739', '9100f02ada0459792e3305feddda602e3278833a', 'v0.0.303'),
    ('xdensenet40_2_k24_bc_cifar10', '0531', 'd3c448ab2c110f873579093ff9a69e735d80b4e7', 'v0.0.226'),
    ('xdensenet40_2_k24_bc_cifar100', '2396', '84357bb40bcd1da5cf6237ea5755a309bcf36d49', 'v0.0.227'),
    ('xdensenet40_2_k24_bc_svhn', '0287', '065f384765a1eaaba26d1d9224878658cbb9cb84', 'v0.0.306'),
    ('xdensenet40_2_k36_bc_cifar10', '0437', 'fb6d7431c005eb9965da0e1b2872c048d6b31b30', 'v0.0.233'),
    ('xdensenet40_2_k36_bc_cifar100', '2165', '9ac51e902167ba05f1c21ed1a9690c1fd4cad3eb', 'v0.0.234'),
    ('xdensenet40_2_k36_bc_svhn', '0274', 'bf7f7de9f9b9661385a47b5e241fdc0c54287a8c', 'v0.0.306'),
    ('wrn16_10_cifar10', '0293', '4ac60015e3b287580d11e605793b3426e8184137', 'v0.0.166'),
    ('wrn16_10_cifar100', '1895', 'd6e852788e29532c8a12bb39617a2e81aba2483f', 'v0.0.204'),
    ('wrn16_10_svhn', '0278', 'b87185c815b64a1290ecbb7a217447906c77da75', 'v0.0.271'),
    ('wrn28_10_cifar10', '0239', 'f8a24941ca542f78eda2d192f461b1bac0600d27', 'v0.0.166'),
    ('wrn28_10_cifar100', '1788', '603872998b7d9f0303769cb34c4cfd16d4e09258', 'v0.0.320'),
    ('wrn28_10_svhn', '0271', '59f255be865678bc0d3c7dcc9785022f30265d69', 'v0.0.276'),
    ('wrn40_8_cifar10', '0237', '3f56f24a07be7155fb143cc4360755d564e3761a', 'v0.0.166'),
    ('wrn40_8_cifar100', '1803', '794aca6066fb993f2a5511df45fca58d6bc546e7', 'v0.0.321'),
    ('wrn40_8_svhn', '0254', '8af6aad0c2034ed8a574f74391869a0d20def51b', 'v0.0.277'),
    ('wrn20_10_1bit_cifar10', '0326', '3288c59a265fc3531502b9c53e33322ff74dd33f', 'v0.0.302'),
    ('wrn20_10_1bit_cifar100', '1904', '1c6f1917c49134da366abfbd27c1d7ad61182882', 'v0.0.302'),
    ('wrn20_10_1bit_svhn', '0273', '4d7bfe0dfa88d593f691b39ca9d20eb3e78636ea', 'v0.0.302'),
    ('wrn20_10_32bit_cifar10', '0314', '90b3fc15d99009b35b1939baefa2e2290003968a', 'v0.0.302'),
    ('wrn20_10_32bit_cifar100', '1812', '346f276fe7e6b61cc93482fdb3d471064d1e1de3', 'v0.0.302'),
    ('wrn20_10_32bit_svhn', '0259', 'af3fddd1f68f373038eea1828e7ae15d21a03ef9', 'v0.0.302'),
    ('ror3_56_cifar10', '0543', '7ca1b24c4a573d53484ca92b19bad5c08e38fa8b', 'v0.0.228'),
    ('ror3_56_cifar100', '2549', 'a7903e5f5f80bf53c07e12ce34659e0d9af4b106', 'v0.0.229'),
    ('ror3_56_svhn', '0269', '113859bb3c23fde05fce740647a26dca69678a34', 'v0.0.287'),
    ('ror3_110_cifar10', '0435', 'bf021f253fc1cf29b30a1eb579c7c4693f963933', 'v0.0.235'),
    ('ror3_110_cifar100', '2364', '13de922a8f8758a15eaf1d283dc42e7dcf0f3fda', 'v0.0.236'),
    ('ror3_110_svhn', '0257', '4b8b6963fd73753104945853a65210de84c9fb4c', 'v0.0.287'),
    ('ror3_164_cifar10', '0393', '7ac7b44610acdb065f40b62e94d5ec5dbb49ee11', 'v0.0.294'),
    ('ror3_164_cifar100', '2234', 'd5a5321048d06f554a8c7688b743c32da830372b', 'v0.0.294'),
    ('ror3_164_svhn', '0273', '1d0a2f127a194ea923857c1d8ec732ae5fa87300', 'v0.0.294'),
    ('rir_cifar10', '0328', '9780c77d0ab1c63478531557ab1aff77c208ad0d', 'v0.0.292'),
    ('rir_cifar100', '1923', '4bfd2f239ecca391c116cbc02d2ef7e5e2a54028', 'v0.0.292'),
    ('rir_svhn', '0268', '5240bc967aa1fc1e9df2b31919178203dcaa582a', 'v0.0.292'),
    ('shakeshakeresnet20_2x16d_cifar10', '0515', 'e2f524b5196951f48495973a087135ca974ec327', 'v0.0.215'),
    ('shakeshakeresnet20_2x16d_cifar100', '2922', '84772a31f6f6bb3228276515a8d4371c25925c85', 'v0.0.247'),
    ('shakeshakeresnet20_2x16d_svhn', '0317', '261fd59fcb7cf375331ce0c402ad2030b283c17c', 'v0.0.295'),
    ('shakeshakeresnet26_2x32d_cifar10', '0317', '5422fce187dff99fa8f4678274a8dd1519e23e27', 'v0.0.217'),
    ('shakeshakeresnet26_2x32d_cifar100', '1880', '750a574e738cf53079b6965410e07fb3abef82fd', 'v0.0.222'),
    ('shakeshakeresnet26_2x32d_svhn', '0262', '844e1f6d067b830087b9456617159a77137138f7', 'v0.0.295'),
    ('diaresnet20_cifar10', '0622', '1c5f4c8adeb52090b5d1ee7330f02b96d4aac843', 'v0.0.340'),
    ('diaresnet20_cifar100', '2771', '350c5ed4fa58bf339b8b44f19044d75ee14917cf', 'v0.0.342'),
    ('diaresnet20_svhn', '0323', 'f37bac8b8843319d2934a79e62c0e7365addef2f', 'v0.0.342'),
    ('diaresnet56_cifar10', '0505', '4073bb0c53d239a40c6cf7ee634f32096b1d54dd', 'v0.0.340'),
    ('diaresnet56_cifar100', '2435', '22e777d2b708b1fc8eb79e593130fa660b51dd95', 'v0.0.342'),
    ('diaresnet56_svhn', '0268', '7ea0022b7eff7afd1bb53e81d579e23952f9ee7f', 'v0.0.342'),
    ('diaresnet110_cifar10', '0410', '5d0517456f3d535722d4f3fade53146ffd8e9f5f', 'v0.0.340'),
    ('diaresnet110_cifar100', '2211', '4c6aa3fe0a58d54ce04061df8440b798b73c9c4b', 'v0.0.342'),
    ('diaresnet110_svhn', '0247', '515ce8f3ddc01b00747b839e8b52387f231f482f', 'v0.0.342'),
    ('diaresnet164bn_cifar10', '0350', '27cfe80d62974bfc1d3aa52e1fd1d173d5067393', 'v0.0.340'),
    ('diaresnet164bn_cifar100', '1953', '18aa50ab105095688597937fcafdbae1d5518597', 'v0.0.342'),
    ('diaresnet164bn_svhn', '0244', '4773b5183a25ef906e176079f3cae8641a167e13', 'v0.0.342'),
    ('diapreresnet20_cifar10', '0642', 'bfcfd5c633e563036061d10d420ea6878f102ddb', 'v0.0.343'),
    ('diapreresnet20_cifar100', '2837', '936a4acca4a570be185c6338e0a76c8d8cee78a9', 'v0.0.343'),
    ('diapreresnet20_svhn', '0303', 'd682b80f3a2f5d126eac829dc3a55d800a6e3998', 'v0.0.343'),
    ('diapreresnet56_cifar10', '0483', 'd5229916f76180aa66a08d89645c1cdd1bbf4bf1', 'v0.0.343'),
    ('diapreresnet56_cifar100', '2505', '9867b907f721c3688bc9577e2d30e71aac14e163', 'v0.0.343'),
    ('diapreresnet56_svhn', '0280', '7a984a6375979ecce61576cc371ed5170a4b2cd2', 'v0.0.343'),
    ('diapreresnet110_cifar10', '0425', '9fab76b9a11b246b0e06386879b29196af002de5', 'v0.0.343'),
    ('diapreresnet110_cifar100', '2269', '0af00d413f9c7022ebec87256760b40ccb30e944', 'v0.0.343'),
    ('diapreresnet110_svhn', '0242', '2bab754f7a7d426eb5a1f40c3156e2c82aa145c2', 'v0.0.343'),
    ('diapreresnet164bn_cifar10', '0356', '7a0b124307fe307489743d8648e99239e14b764a', 'v0.0.343'),
    ('diapreresnet164bn_cifar100', '1999', 'a3835edf5ae8daa0383e8d13fedf3a8dc8352338', 'v0.0.343'),
    ('diapreresnet164bn_svhn', '0256', '30de9b3b60e03ab5c44bf7d9b571f63a9065890d', 'v0.0.343'),
    ('resnet10_cub', '2760', 'e8bdefb0f503d253197370a2d9d5ae772b2cb913', 'v0.0.335'),
    ('resnet12_cub', '2667', '22b2b21696461aa952a257014f4f0ec901375ac5', 'v0.0.336'),
    ('resnet14_cub', '2434', '57f6a73d2eb22d7dfc43a8ff52f25982e1b7d78b', 'v0.0.337'),
    ('resnet16_cub', '2321', '5e48b19f8fb8eae1afcdf04e77ae3ad9ad9c6b73', 'v0.0.338'),
    ('resnet18_cub', '2333', 'c32998b4b12e31b9d291770bbf3eb38490542e38', 'v0.0.344'),
    ('resnet26_cub', '2261', '56c8fcc12333fec68ac09c6696bb462e175be047', 'v0.0.345'),
    ('seresnet10_cub', '2742', 'b8e56acfe873705609c82932c321467169436531', 'v0.0.361'),
    ('seresnet12_cub', '2599', '9c0ee8cf33733bf5ba66eeda7394c84ed11d3d7e', 'v0.0.361'),
    ('seresnet14_cub', '2368', 'b58cddb7b2cc8f5c40a83912690eeff8d4d6d418', 'v0.0.361'),
    ('seresnet16_cub', '2318', '1d8b187c417832ac3f19806ff13f1897c7692f4f', 'v0.0.361'),
    ('seresnet18_cub', '2321', '7b1d02a7965a3f54606d768e0e5149148f2fb0b1', 'v0.0.361'),
    ('seresnet26_cub', '2254', '5cbf65d229088b3f16e396a05bde054470c14563', 'v0.0.361'),
    ('mobilenet_w1_cub', '2356', '02c2accf0f92fcc460cdbb6b41a581321e1fa216', 'v0.0.346'),
    ('proxylessnas_mobile_cub', '2190', 'a9c66b1b9623f81105b9daf8c5e45f4501e80bbe', 'v0.0.347'),
    ('ntsnet_cub', '1286', '4d7595248f0fb042ef06c657d73bd0a2f3fc4f0d', 'v0.0.334'),
    ('pspnet_resnetd101b_voc', '7626', 'f90c0db9892ec6892623a774ba21000f7cc3995f', 'v0.0.297'),
    ('pspnet_resnetd50b_ade20k', '2746', '7b7ce5680fdfab567222ced11a2430cf1a452116', 'v0.0.297'),
    ('pspnet_resnetd101b_ade20k', '3286', 'c5e619c41740751865f662b539abbad5dd9be42b', 'v0.0.297'),
    ('pspnet_resnetd101b_cityscapes', '5757', '2e2315d45b83479c507a4e7a47dac6a68a8e3e1c', 'v0.0.297'),
    ('pspnet_resnetd101b_coco', '5467', '690335581310128a1d11fcdb0eb03ce07fb5f88d', 'v0.0.297'),
    ('deeplabv3_resnetd101b_voc', '7566', '6a4f805fe1433898d1dc665bb10a5620816999bd', 'v0.0.298'),
    ('deeplabv3_resnetd152b_voc', '7806', '1c3089b5034043e4a82567ae28b085d694e5319c', 'v0.0.298'),
    ('deeplabv3_resnetd50b_ade20k', '3196', '00903dce3d63fd847c36617d51907cff12834d06', 'v0.0.298'),
    ('deeplabv3_resnetd101b_ade20k', '3517', '46828740498741a7291fd479901dfba3d3de3b11', 'v0.0.298'),
    ('deeplabv3_resnetd101b_coco', '5906', '2811b3cd3512c237faef59f746d984823892d9e5', 'v0.0.298'),
    ('deeplabv3_resnetd152b_coco', '6107', '80ddcd964c41906f4bc104cf5b087303a06aa79f', 'v0.0.298'),
    ('fcn8sd_resnetd101b_voc', '8040', '3568dc41c137cbe797c1baa7b5a76669faf1ceb0', 'v0.0.299'),
    ('fcn8sd_resnetd50b_ade20k', '3339', '1d03bc38ea64551806ddfd4185b5eb49fb9e160f', 'v0.0.299'),
    ('fcn8sd_resnetd101b_ade20k', '3588', 'ff385e1913bc8c05c6abe9cb19896f477b9b75a7', 'v0.0.299'),
    ('fcn8sd_resnetd101b_coco', '6011', '4a469997cdc3e52c1dee1a2d58578f9df54c419b', 'v0.0.299'),
]}

imgclsmob_repo_url = 'https://github.com/osmr/imgclsmob'


def get_model_name_suffix_data(model_name):
    if model_name not in _model_sha1:
        raise ValueError("Pretrained model for {name} is not available.".format(name=model_name))
    error, sha1_hash, repo_release_tag = _model_sha1[model_name]
    return error, sha1_hash, repo_release_tag


def get_model_file(model_name,
                   local_model_store_dir_path=os.path.join("~", ".chainer", "models")):
    """
    Return location for the pretrained on local file system. This function will download from online model zoo when
    model cannot be found or has mismatch. The root directory will be created if it doesn't exist.

    Parameters
    ----------
    model_name : str
        Name of the model.
    local_model_store_dir_path : str, default $CHAINER_HOME/models
        Location for keeping the model parameters.

    Returns
    -------
    file_path
        Path to the requested pretrained model file.
    """
    error, sha1_hash, repo_release_tag = get_model_name_suffix_data(model_name)
    short_sha1 = sha1_hash[:8]
    file_name = "{name}-{error}-{short_sha1}.npz".format(
        name=model_name,
        error=error,
        short_sha1=short_sha1)
    local_model_store_dir_path = os.path.expanduser(local_model_store_dir_path)
    file_path = os.path.join(local_model_store_dir_path, file_name)
    if os.path.exists(file_path):
        if _check_sha1(file_path, sha1_hash):
            return file_path
        else:
            logging.warning("Mismatch in the content of model file detected. Downloading again.")
    else:
        logging.info("Model file not found. Downloading to {}.".format(file_path))

    if not os.path.exists(local_model_store_dir_path):
        os.makedirs(local_model_store_dir_path)

    zip_file_path = file_path + ".zip"
    _download(
        url="{repo_url}/releases/download/{repo_release_tag}/{file_name}.zip".format(
            repo_url=imgclsmob_repo_url,
            repo_release_tag=repo_release_tag,
            file_name=file_name),
        path=zip_file_path,
        overwrite=True)
    with zipfile.ZipFile(zip_file_path) as zf:
        zf.extractall(local_model_store_dir_path)
    os.remove(zip_file_path)

    if _check_sha1(file_path, sha1_hash):
        return file_path
    else:
        raise ValueError("Downloaded file has different hash. Please try again.")


def _download(url, path=None, overwrite=False, sha1_hash=None, retries=5, verify_ssl=True):
    """Download an given URL

    Parameters
    ----------
    url : str
        URL to download
    path : str, optional
        Destination path to store downloaded file. By default stores to the
        current directory with same name as in url.
    overwrite : bool, optional
        Whether to overwrite destination file if already exists.
    sha1_hash : str, optional
        Expected sha1 hash in hexadecimal digits. Will ignore existing file when hash is specified
        but doesn't match.
    retries : integer, default 5
        The number of times to attempt the download in case of failure or non 200 return codes
    verify_ssl : bool, default True
        Verify SSL certificates.

    Returns
    -------
    str
        The file path of the downloaded file.
    """
    import warnings
    try:
        import requests
    except ImportError:
        class requests_failed_to_import(object):
            pass
        requests = requests_failed_to_import

    if path is None:
        fname = url.split("/")[-1]
        # Empty filenames are invalid
        assert fname, "Can't construct file-name from this URL. Please set the `path` option manually."
    else:
        path = os.path.expanduser(path)
        if os.path.isdir(path):
            fname = os.path.join(path, url.split("/")[-1])
        else:
            fname = path
    assert retries >= 0, "Number of retries should be at least 0"

    if not verify_ssl:
        warnings.warn(
            "Unverified HTTPS request is being made (verify_ssl=False). "
            "Adding certificate verification is strongly advised.")

    if overwrite or not os.path.exists(fname) or (sha1_hash and not _check_sha1(fname, sha1_hash)):
        dirname = os.path.dirname(os.path.abspath(os.path.expanduser(fname)))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        while retries + 1 > 0:
            # Disable pyling too broad Exception
            # pylint: disable=W0703
            try:
                print("Downloading {} from {}...".format(fname, url))
                r = requests.get(url, stream=True, verify=verify_ssl)
                if r.status_code != 200:
                    raise RuntimeError("Failed downloading url {}".format(url))
                with open(fname, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                if sha1_hash and not _check_sha1(fname, sha1_hash):
                    raise UserWarning("File {} is downloaded but the content hash does not match."
                                      " The repo may be outdated or download may be incomplete. "
                                      "If the 'repo_url' is overridden, consider switching to "
                                      "the default repo.".format(fname))
                break
            except Exception as e:
                retries -= 1
                if retries <= 0:
                    raise e
                else:
                    print("download failed, retrying, {} attempt{} left"
                          .format(retries, "s" if retries > 1 else ""))

    return fname


def _check_sha1(filename, sha1_hash):
    """Check whether the sha1 hash of the file content matches the expected hash.

    Parameters
    ----------
    filename : str
        Path to the file.
    sha1_hash : str
        Expected sha1 hash in hexadecimal digits.

    Returns
    -------
    bool
        Whether the file content matches the expected hash.
    """
    sha1 = hashlib.sha1()
    with open(filename, "rb") as f:
        while True:
            data = f.read(1048576)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest() == sha1_hash
