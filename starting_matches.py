from espncricinfo.match import Match
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# # this code has been commented out to facilitate a faster run-time, but the code to produce the list of match IDs is
# # below
#
# # list of years since the T20 Format was introduced to International Cricket in 2005
# years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
#          '2018', '2019', '2020', '2021', '2022']
#
# match_ids = []
#
# # scrapes data from each year of T20I matches and adds the Match IDs for the year to a list
# for year in years:
#     url = 'https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=' + year + ';type=year'
#     reqs = requests.get(url)
#     soup = BeautifulSoup(reqs.text, 'html.parser')
#     matches = soup.find_all(class_='data1')
#     for match in matches:
#         link_in_html = match.find_all('a')[-1]
#         link = link_in_html.get('href')
#         match_id_finder = re.search('/ci/engine/match/(.*).html', link)
#         match_id = match_id_finder.group(1)
#         match_ids.append(match_id)

# the list produced as a result of the code above
# this list includes all Match IDs before the start of the 2022 ICC T20I World Cup
match_ids = ['211048', '211028', '222678', '226374', '237242', '238195', '225271', '225263', '264065', '255954',
             '251487', '251488', '249227', '255957', '258463', '258464', '306987', '306989', '306991', '287853',
             '287854', '287855', '287856', '287857', '287858', '287859', '287860', '287861', '287862', '287863',
             '287864', '287865', '287866', '287867', '287868', '287869', '287870', '287871', '287872', '287873',
             '287874', '287875', '287876', '287877', '287878', '287879', '297800', '298795', '291343', '319112',
             '298804', '291356', '300435', '300436', '343764', '296903', '319142', '354453', '354454', '354455',
             '354456', '354457', '354458', '361530', '361531', '354459', '354460', '354461', '361653', '361654',
             '361655', '361656', '361657', '361658', '361659', '361660', '350347', '366707', '366708', '351694',
             '351695', '386535', '351696', '386494', '366622', '352674', '350475', '350476', '392615', '355991',
             '355992', '355993', '355994', '355995', '355996', '355997', '355998', '355999', '356000', '356002',
             '356001', '356003', '356004', '356005', '356006', '356007', '356008', '356009', '356010', '356012',
             '356011', '356013', '356014', '356015', '356016', '356017', '401076', '403375', '350050', '403385',
             '403386', '426723', '426724', '387563', '387564', '430884', '430885', '440224', '440100', '440218',
             '423782', '440219', '441640', '406207', '439495', '439497', '439500', '439499', '439506', '439505',
             '439507', '439510', '439511', '440945', '440946', '406197', '406198', '423787', '423788', '439139',
             '412678', '412677', '412679', '412680', '412682', '412683', '412686', '412685', '412684', '412681',
             '412688', '412687', '412689', '412690', '412691', '412692', '412693', '412694', '412695', '412696',
             '412697', '412698', '412699', '412700', '412701', '412702', '412703', '439146', '447539', '456991',
             '456992', '452153', '452154', '426392', '426393', '426417', '426418', '463141', '463142', '478279',
             '461565', '446956', '473918', '473919', '473920', '463149', '446960', '446961', '489212', '489220',
             '474466', '516204', '516205', '474476', '523735', '523736', '525816', '525817', '531982', '514023',
             '527012', '514024', '527013', '521217', '530432', '538068', '518954', '518955', '520595', '520596',
             '520597', '520598', '520599', '543883', '543884', '531635', '543885', '531636', '531637', '546410',
             '546411', '546414', '546418', '546443', '546442', '546462', '546463', '546470', '546473', '546477',
             '540173', '556252', '540174', '562437', '562438', '534208', '560921', '560922', '567071', '567072',
             '567073', '567204', '567205', '573672', '564786', '571148', '571149', '534233', '571150', '534234',
             '565820', '534235', '533272', '533273', '533274', '533275', '533276', '533277', '533278', '533279',
             '533280', '533281', '533282', '533283', '533284', '533285', '533286', '533287', '533288', '533289',
             '533290', '533291', '533292', '533293', '533294', '533295', '533296', '533297', '533298', '582186',
             '587476', '565810', '567353', '565811', '567354', '589306', '567355', '589307', '573019', '573020',
             '569237', '569238', '573027', '569239', '593986', '567367', '592272', '593987', '592273', '592268',
             '592269', '602477', '630951', '592276', '623571', '623572', '566926', '566927', '631573', '631574',
             '645645', '645647', '635658', '635659', '635660', '659545', '659547', '566937', '566938', '662383',
             '647247', '662387', '668959', '649101', '660107', '649103', '660123', '660113', '660149', '685727',
             '668969', '660173', '685729', '660185', '660203', '660209', '660223', '660235', '657631', '657633',
             '657635', '661695', '661697', '636164', '636165', '636166', '690351', '690353', '702141', '702143',
             '636536', '636537', '648681', '636538', '648683', '682897', '682899', '682901', '682903', '682905',
             '682907', '682909', '682911', '682913', '682915', '682917', '682919', '682921', '682923', '682925',
             '682927', '682929', '682931', '682933', '682935', '682937', '682939', '682941', '682943', '682945',
             '682947', '682949', '682951', '682953', '682955', '682957', '682959', '682961', '682963', '682965',
             '667887', '730283', '730285', '730293', '667731', '727917', '754717', '754719', '754721', '802327',
             '742617', '754039', '722335', '722337', '736063', '858491', '868723', '868725', '876463', '876465',
             '889463', '876467', '743953', '883341', '883343', '883345', '883347', '817203', '817205', '875457',
             '875459', '875467', '875471', '875481', '875485', '875491', '875501', '875507', '875513', '885969',
             '875521', '885971', '875541', '875545', '875549', '875551', '875553', '860279', '860281', '894293',
             '848839', '848841', '743975', '919603', '919605', '903587', '903589', '924637', '924639', '915783',
             '915785', '931396', '931398', '930575', '930573', '930577', '930579', '902649', '902651', '930581',
             '930583', '930585', '902653', '914217', '953345', '914219', '953347', '914221', '958415', '914223',
             '958417', '958419', '914225', '958421', '895817', '895819', '953103', '953105', '895821', '967081',
             '966373', '966375', '954733', '954735', '954737', '963697', '963699', '954741', '963701', '954743',
             '966713', '966735', '800479', '966737', '966739', '800481', '966741', '966743', '966745', '966747',
             '966749', '966751', '966753', '966755', '966757', '966759', '966761', '966763', '884347', '884349',
             '966765', '951305', '951307', '951309', '951311', '884351', '951313', '951315', '951317', '951319',
             '951321', '951323', '951325', '951327', '951329', '951333', '951331', '951335', '951337', '951339',
             '951341', '951343', '951345', '951347', '951349', '951351', '951353', '951355', '951357', '951359',
             '951361', '951365', '951363', '951367', '951369', '951371', '951373', '1007655', '1007657', '1007659',
             '913633', '1041615', '1041617', '1004729', '995467', '913663', '995469', '1050217', '1050219', '1050221',
             '1072206', '1072207', '1072208', '1019979', '1019981', '1019983', '1074957', '1074958', '1074959',
             '1074961', '1074962', '1074964', '1074965', '1074966', '1074968', '1074969', '1074970', '1074971',
             '936153', '936155', '936157', '1034825', '1034827', '1034829', '1020029', '1001349', '1001351', '1001353',
             '1040485', '1040487', '1040489', '1077947', '1077948', '1085495', '1085496', '1083449', '1083450',
             '1089202', '1089203', '1089243', '1089776', '1089777', '1089778', '1031431', '1031433', '1031435',
             '1098211', '1109610', '1117821', '1117822', '1117824', '1031665', '1119501', '1119502', '1120291',
             '1075507', '1120292', '1075508', '1120293', '1120093', '1120094', '1120095', '1122729', '1122730',
             '1122731', '1115798', '1115799', '1115800', '1115807', '1115808', '1115809', '1072316', '1134031',
             '1134032', '1072317', '1072318', '1072319', '1130746', '1072320', '1072321', '1130747', '1122285',
             '1072322', '1122286', '1122287', '1133817', '1133818', '1133819', '1133820', '1133821', '1133822',
             '1133823', '1140069', '1140070', '1140071', '1141232', '1145982', '1145983', '1145984', '1142501',
             '1127300', '1142502', '1127301', '1142503', '1142504', '1142505', '1142506', '1140992', '1119542',
             '1140993', '1142913', '1142914', '1142915', '1119543', '1142916', '1142917', '1142918', '1119544',
             '1142919', '1119545', '1141835', '1146723', '1146724', '1146725', '1142589', '1150143', '1150144',
             '1144149', '1144150', '1162727', '1157372', '1157373', '1140384', '1157374', '1157375', '1157376',
             '1157759', '1157377', '1157760', '1157761', '1144989', '1144990', '1144991', '1144992', '1153317',
             '1153318', '1153319', '1153843', '1171752', '1171753', '1171754', '1171755', '1171756', '1171757',
             '1171758', '1171759', '1171760', '1171761', '1171762', '1170457', '1170458', '1144161', '1170459',
             '1144162', '1153696', '1144163', '1153697', '1153698', '1172505', '1172506', '1172507', '1172508',
             '1172509', '1172510', '1168112', '1168113', '1168114', '1168247', '1168248', '1158071', '1158072',
             '1158073', '1177484', '1177485', '1144172', '1176792', '1176793', '1144173', '1176794', '1176795',
             '1176796', '1176797', '1144174', '1175344', '1175346', '1181405', '1181406', '1181407', '1181408',
             '1181410', '1181409', '1152840', '1183920', '1183921', '1183922', '1184259', '1184258', '1184260',
             '1184262', '1184263', '1184261', '1184900', '1184901', '1184902', '1184266', '1178995', '1178996',
             '1185200', '1185201', '1185202', '1185179', '1185180', '1185181', '1185183', '1185184', '1185185',
             '1185186', '1185182', '1185187', '1185189', '1185191', '1185192', '1185193', '1189743', '1185188',
             '1189744', '1185190', '1188379', '1186488', '1186489', '1188380', '1186490', '1186491', '1186492',
             '1186493', '1192556', '1192557', '1192558', '1192811', '1192812', '1192813', '1192814', '1192816',
             '1192815', '1168521', '1192818', '1192223', '1192823', '1192824', '1192224', '1168522', '1190767',
             '1190768', '1190769', '1190771', '1190772', '1190773', '1190774', '1190775', '1190776', '1191005',
             '1188621', '1188622', '1191006', '1191007', '1188623', '1191008', '1195132', '1195133', '1195134',
             '1197396', '1197397', '1197507', '1197398', '1197399', '1197508', '1197400', '1197401', '1197509',
             '1197402', '1197403', '1197510', '1197404', '1197405', '1197406', '1197407', '1197842', '1197843',
             '1197841', '1197844', '1197845', '1197846', '1198898', '1198899', '1198900', '1198901', '1198902',
             '1192875', '1192876', '1192877', '1197140', '1197141', '1197142', '1200425', '1200426', '1197143',
             '1200427', '1187005', '1200428', '1197144', '1200429', '1197145', '1187006', '1201680', '1201681',
             '1202007', '1201682', '1202008', '1201683', '1202009', '1202010', '1201685', '1200202', '1200203',
             '1200204', '1202011', '1200205', '1200206', '1200207', '1197520', '1197521', '1200208', '1200209',
             '1198489', '1200210', '1200211', '1197522', '1197523', '1200212', '1197524', '1197525', '1198490',
             '1197526', '1197527', '1198491', '1202014', '1197528', '1197529', '1202015', '1202016', '1203831',
             '1203832', '1203833', '1202026', '1199499', '1199500', '1199501', '1204616', '1199502', '1199503',
             '1199504', '1199505', '1199506', '1199507', '1202028', '1199508', '1199509', '1199510', '1199511',
             '1199512', '1199513', '1199514', '1199515', '1199516', '1199517', '1199518', '1199519', '1199520',
             '1199521', '1199522', '1199523', '1199524', '1199525', '1199526', '1199527', '1199528', '1199529',
             '1199530', '1199531', '1201668', '1199532', '1199533', '1201669', '1199534', '1201670', '1201671',
             '1199535', '1183524', '1199536', '1199537', '1201672', '1199538', '1199539', '1201673', '1199540',
             '1199541', '1199542', '1183525', '1199543', '1199544', '1199545', '1187665', '1183526', '1199546',
             '1199547', '1199548', '1199549', '1187666', '1183527', '1187013', '1187667', '1183528', '1205260',
             '1205261', '1205262', '1205263', '1187014', '1187668', '1183529', '1205264', '1205265', '1187669',
             '1205266', '1187015', '1193494', '1193495', '1193496', '1208606', '1208609', '1187018', '1208612',
             '1187019', '1208613', '1187020', '1202242', '1202243', '1202244', '1203676', '1203677', '1203678',
             '1187677', '1213058', '1213059', '1187678', '1187679', '1187680', '1187681', '1215133', '1185313',
             '1215134', '1185314', '1215135', '1185315', '1215136', '1215137', '1185316', '1215152', '1215151',
             '1215154', '1215153', '1215138', '1185317', '1215155', '1215156', '1215139', '1215158', '1215157',
             '1215159', '1215160', '1215161', '1215162', '1215140', '1215163', '1215164', '1185318', '1215165',
             '1217738', '1217739', '1217740', '1217741', '1217742', '1217743', '1217744', '1217745', '1213874',
             '1217747', '1216416', '1213875', '1216417', '1207081', '1207082', '1214670', '1216418', '1214671',
             '1229824', '1229818', '1198244', '1229819', '1229820', '1229821', '1229822', '1229823', '1198245',
             '1198246', '1198235', '1198236', '1198237', '1233064', '1233065', '1233066', '1235829', '1235830',
             '1235831', '1235832', '1233464', '1233465', '1233466', '1233954', '1237122', '1233955', '1237123',
             '1233956', '1237124', '1223952', '1223953', '1223954', '1233959', '1233960', '1233961', '1243019',
             '1243020', '1243021', '1233971', '1233972', '1233973', '1252066', '1233974', '1252067', '1233975',
             '1252068', '1243388', '1243389', '1243390', '1252058', '1243391', '1252059', '1252060', '1243392',
             '1233979', '1233980', '1233981', '1257404', '1257405', '1257406', '1251575', '1251576', '1251577',
             '1251578', '1257945', '1257946', '1257947', '1257948', '1257949', '1257183', '1257950', '1257184',
             '1257951', '1257185', '1263708', '1263709', '1263710', '1263711', '1263712', '1263713', '1249206',
             '1267305', '1267304', '1249207', '1267306', '1267307', '1267308', '1267309', '1267310', '1249208',
             '1267311', '1263151', '1267312', '1263152', '1263153', '1263154', '1263155', '1268188', '1268189',
             '1268190', '1263156', '1268191', '1268192', '1263157', '1263158', '1263159', '1239540', '1263160',
             '1239541', '1251953', '1239542', '1267680', '1251954', '1267681', '1269836', '1269837', '1251955',
             '1269838', '1267682', '1262758', '1263164', '1262759', '1262760', '1263165', '1263166', '1270834',
             '1263167', '1270835', '1271445', '1271446', '1271447', '1270836', '1271448', '1270837', '1271449',
             '1271450', '1271451', '1270838', '1273132', '1273133', '1273134', '1273141', '1273142', '1273135',
             '1273143', '1273136', '1273144', '1273146', '1273137', '1273145', '1273147', '1273138', '1273148',
             '1273139', '1273149', '1273140', '1272373', '1272374', '1272093', '1272375', '1275269', '1275270',
             '1275267', '1272376', '1275268', '1275271', '1272094', '1275272', '1275273', '1275274', '1275275',
             '1272377', '1275277', '1272095', '1275276', '1272096', '1275041', '1275052', '1272097', '1275044',
             '1271630', '1275039', '1275053', '1275040', '1275054', '1271631', '1275043', '1275042', '1271632',
             '1275046', '1275047', '1273271', '1275045', '1275051', '1273272', '1273273', '1280057', '1279379',
             '1279380', '1279381', '1279382', '1280060', '1279383', '1279384', '1280061', '1279385', '1280063',
             '1279386', '1280058', '1280062', '1280059', '1282738', '1282739', '1283021', '1283022', '1282740',
             '1283023', '1283024', '1282741', '1283025', '1283026', '1282742', '1273712', '1283027', '1283028',
             '1282743', '1273713', '1273714', '1273715', '1283029', '1283030', '1282744', '1283089', '1273716',
             '1283031', '1283032', '1282745', '1273717', '1283033', '1283034', '1282746', '1283090', '1273718',
             '1283035', '1283036', '1282747', '1273719', '1283037', '1282748', '1273720', '1282272', '1283091',
             '1282749', '1273721', '1283038', '1283039', '1282273', '1273722', '1283040', '1283041', '1282275',
             '1273723', '1282274', '1284488', '1283092', '1282276', '1273724', '1284489', '1282277', '1273725',
             '1284490', '1282278', '1273726', '1284491', '1282279', '1283093', '1273727', '1284492', '1282281',
             '1273728', '1283094', '1273729', '1273730', '1284493', '1273731', '1284494', '1273732', '1284495',
             '1273733', '1284496', '1273734', '1284497', '1273735', '1273736', '1273737', '1273738', '1273739',
             '1273740', '1283042', '1273741', '1283043', '1273742', '1283044', '1273743', '1283045', '1273744',
             '1273745', '1273746', '1283046', '1273747', '1283047', '1273748', '1283048', '1273749', '1283049',
             '1273750', '1283050', '1273751', '1283051', '1286667', '1286668', '1273752', '1286669', '1286670',
             '1286671', '1273753', '1286672', '1286673', '1286677', '1286675', '1273754', '1286674', '1286676',
             '1286678', '1286679', '1273755', '1286680', '1286681', '1286682', '1286683', '1286684', '1286685',
             '1286686', '1273756', '1286687', '1289042', '1289043', '1289044', '1289045', '1278671', '1289046',
             '1289047', '1289048', '1289049', '1277974', '1278672', '1289050', '1289051', '1277975', '1289052',
             '1289053', '1278673', '1277976', '1287773', '1287774', '1287775', '1291187', '1291188', '1256720',
             '1256721', '1256722', '1256723', '1256724', '1263471', '1299593', '1299638', '1299594', '1299592',
             '1263472', '1299595', '1299596', '1263473', '1278679', '1299567', '1299566', '1263474', '1299569',
             '1299568', '1278680', '1299571', '1299570', '1299573', '1299572', '1263475', '1278681', '1299575',
             '1299574', '1299576', '1299577', '1299579', '1299578', '1299580', '1299581', '1299582', '1299583',
             '1299585', '1299584', '1278684', '1278685', '1278686', '1299832', '1299833', '1305498', '1305499',
             '1305500', '1305501', '1305502', '1305503', '1305504', '1288316', '1309701', '1309702', '1309703',
             '1310156', '1310157', '1310158', '1310159', '1310160', '1310161', '1310162', '1310163', '1310164',
             '1310165', '1310166', '1310167', '1310168', '1310169', '1310170', '1310171', '1310172', '1310173',
             '1310174', '1310175', '1310176', '1310177', '1310178', '1310179', '1310180', '1310181', '1310182',
             '1310183', '1310184', '1310185', '1310186', '1310187', '1310938', '1310939', '1310188', '1310189',
             '1310940', '1310190', '1310941', '1310942', '1317140', '1317141', '1317142', '1307293', '1307294',
             '1318357', '1278687', '1318358', '1318359', '1318360', '1318354', '1318352', '1318361', '1310946',
             '1318355', '1318353', '1307295', '1318362', '1318356', '1318363', '1310947', '1278688', '1310948',
             '1278689', '1278690', '1317134', '1317135', '1278691', '1317136', '1317137', '1317138', '1317139',
             '1303307', '1320969', '1320970', '1321311', '1320971', '1320972', '1303308', '1320974', '1320973',
             '1321312', '1320976', '1320975', '1321313', '1320978', '1320977', '1320980', '1320979', '1321998',
             '1320982', '1322011', '1320984', '1317149', '1321999', '1322000', '1320985', '1322012', '1320987',
             '1317150', '1322001', '1322002', '1320986', '1320988', '1322003', '1322004', '1322005', '1322006',
             '1276904', '1317151', '1322007', '1321305', '1321306', '1323550', '1322008', '1322009', '1321307',
             '1323551', '1321308', '1323552', '1276905', '1321309', '1321310', '1276906', '1322010', '1321466',
             '1321465', '1321468', '1321467', '1321470', '1321469', '1321258', '1321257', '1321471', '1321472',
             '1321259', '1321260', '1321262', '1321261', '1321264', '1321263', '1321474', '1321473', '1321476',
             '1321475', '1321478', '1321477', '1321265', '1321266', '1321480', '1321479', '1321267', '1321268',
             '1321270', '1321269', '1321272', '1321271', '1321481', '1321482', '1321483', '1321484', '1321274',
             '1321273', '1321275', '1321276', '1303312', '1321277', '1321278', '1321280', '1321279', '1303313',
             '1303314', '1321281', '1321282', '1321283', '1321284', '1321286', '1321285', '1321287', '1321288',
             '1321289', '1321290', '1321291', '1321292', '1307477', '1276913', '1321294', '1321293', '1321295',
             '1321296', '1276914', '1326825', '1326826', '1307478', '1317903', '1326827', '1321297', '1321298',
             '1323295', '1326828', '1321299', '1321300', '1326829', '1321301', '1321302', '1323296', '1327073',
             '1321304', '1321303', '1276915', '1317904', '1323297', '1317905', '1303315', '1310901', '1310902',
             '1303316', '1317906', '1317907', '1307159', '1317908', '1307160', '1328469', '1307161', '1317909',
             '1328470', '1328471', '1317910', '1307162', '1328472', '1307163', '1328473', '1328849', '1328850',
             '1328851', '1328852', '1328853', '1328854', '1328474', '1328475', '1327269', '1328476', '1327270',
             '1328477', '1328478', '1327271', '1327272', '1327273', '1327274', '1327275', '1327276', '1327277',
             '1327278', '1327279', '1333918', '1333919', '1327280', '1333920', '1333921', '1333922', '1333923',
             '1327281', '1333924', '1333925', '1333926', '1333927', '1333928', '1333929', '1332496', '1332502',
             '1332498', '1332499', '1332500', '1332497', '1332507', '1332503', '1332506', '1332504', '1332505',
             '1332501', '1327503', '1327228', '1332508', '1332509', '1332510', '1327229', '1327504', '1327230',
             '1327505', '1336031', '1327231', '1336032', '1327506', '1327232', '1327233', '1327507', '1327234',
             '1327508', '1317482', '1322334', '1317483', '1322335', '1333930', '1322336', '1317486', '1333931',
             '1333932', '1322337', '1322338', '1317487', '1322339', '1322340', '1317488', '1336951', '1336952',
             ]

# This is the list of Match numbers for the 2021 T20I World Cup. Because there were other T20I tournaments during this
# time, a list is needed to determine if a match is a World Cup Match
wc_2021_match_nums = [1306, 1310, 1311, 1312, 1317, 1321, 1326, 1330, 1333, 1337, 1341, 1345, 1350, 1353, 1356,
                      1360, 1363, 1365, 1367, 1368, 1370, 1372, 1374, 1376, 1377, 1378, 1379, 1380, 1381, 1383, 1385,
                      1387, 1389, 1390, 1391, 1393, 1395, 1397, 1399, 1401, 1405, 1409, 1414, 1419, 1427]

# converts team abbreviation to full team name
cities_to_country = {'Auckland': 'New  Zealand', 'Southampton': 'England', 'Johannesburg': 'South Africa',
                     'Brisbane': 'Australia', 'Bristol': 'England', 'Khulna': 'Bangladesh', 'Wellington': 'New Zealand',
                     'Sydney': 'Australia', 'London': 'England', 'Nairobi': 'Kenya', 'Durban': 'South Africa',
                     'Cape Town': 'South Africa', 'Mumbai': 'India', 'Perth': 'Australia', 'Gqeberha': 'South Africa',
                     'Melbourne': 'Australia', 'Christchurch': 'New Zealand', 'Karachi': 'Pakistan',
                     'Manchester': 'England', 'Bridgetown': 'West Indies', 'Belfast': 'Northern Ireland',
                     'King City': 'Canada', 'Hamilton': 'New Zealand', 'Colombo': 'Sri Lanka',
                     'Port of Spain': 'West Indies', 'Centurion': 'South Africa', 'Dubai': 'UAE',
                     'Nottingham': 'England', 'Basseterre': 'West Indies', 'Nagpur': 'India', 'Chandigarh': 'India',
                     'Abu Dhabi': 'UAE', 'Hobart': 'Australia', 'Providence': 'West Indies',
                     'Gros Islet': 'West Indies', 'North Sound': 'West Indies', 'Lauderhill': 'USA',
                     'Harare': 'Zimbabwe', 'Birmingham': 'England', 'Cardiff': 'Wales', 'Bloemfontein': 'South Africa',
                     'Kimberley': 'South Africa', 'Adelaide': 'Australia', 'Kandy': 'Sri Lanka', 'Dhaka': 'Bangladesh',
                     'Kolkata': 'India', 'Mombasa': 'Kenya', 'Hambantota': 'Sri Lanka', 'The Hague': 'Netherlands',
                     'Chester-le-Street': 'England', 'Chennai': 'India', 'Pune': 'India', 'East London': 'South Africa',
                     'Bengaluru': 'South Africa', 'Ahmedabad': 'India', 'Sharjah': 'UAE', 'Windhoek': 'Namibia',
                     'Bulawayo': 'Zimbabwe', 'Aberdeen': 'Scotland', 'Kingstown': 'West Indies', 'Rajkot': 'India',
                     'Chattogram': 'Bangladesh', 'Kingston': 'West Indies', 'Sylhet': 'Bangladesh',
                     'Roseau': 'West Indies', 'Lahore': 'Pakistan', 'Bready': 'Northern Ireland',
                     'Amstelveen': 'Netherlands', 'Rotterdam': 'Netherlands', 'Edinburgh': 'Scotland',
                     'Dublin': 'Ireland', 'Dharamsala': 'India', 'Cuttack': 'India', 'Mount Maunganui': 'New Zealand',
                     'Mong Kok': 'Hong Kong', 'Townsville': 'Australia', 'Ranchi': 'India', 'Visakhapatnam': 'India',
                     'Fatullah': 'Bangladesh', 'Delhi': 'India', 'Napier': 'New Zealand', 'Kanpur': 'India',
                     'Geelong': 'Australia', 'Greater Noida': 'India', 'Taunton': 'England', 'Guwahati': 'India',
                     'Potchefstroom': 'South Africa', 'Thiruvananthapuram': 'India', 'Indore': 'India',
                     'Nelson': 'New Zealand', 'Dehra Dun': 'India', 'Deventer': 'Netherlands', 'Lucknow': 'India',
                     'Carrara': 'Australia', 'Al Amarat': 'Oman', 'Port Moresby': 'Papua New Guinea', 'Murcia': 'Spain',
                     'Naucalpan': 'Mexico', 'Waterloo': 'Belgium', 'Kampala': 'Uganda', 'Utrecht': 'Netherlands',
                     'St Peter Port': 'Guernsey', 'Castel': 'Guernsey', 'Kuala Lumpur': 'Malaysia', 'Doha': 'Qatar',
                     'Apia': 'Samoa', 'Brondby': 'Denmark', 'Singapore': 'Singapore', 'Kerava': 'Finland',
                     'Ilfov County': 'Romania', 'Lima': 'Peru', 'Corfu': 'Greece', 'Marsa': 'Malta',
                     'Canberra': 'Australia', 'Lilongwe': 'Malawi', 'Blantyre': 'Malawi', 'Kirtipur': 'Nepal',
                     'Hyderabad': 'India', "St George's": 'West Indies', 'Bangkok': 'Thailand', 'Almeria': 'Spain',
                     'Walferdange': 'Luxembourg', 'Sofia': 'Bulgaria', 'Rawalpindi': 'Pakistan',
                     'Paarl': 'South Africa', 'Dunedin': 'New Zealand', 'Coolidge': 'West Indies',
                     'Prague': 'Czech Republic', 'Leeds': 'England', 'Krefeld': 'Germany', 'Kigali City': 'Rwanda',
                     'Albergaria': 'Portugal', 'Entebbe': 'Uganda', 'Episkopi': 'Cyprus', 'Lagos': 'Nigeria',
                     'Jaipur': 'India', 'George Town': 'Cayman Islands', 'Lower Austria': 'Austria', 'Ghent': 'Belgium',
                     'Bangi': 'Malaysia', 'Belgrade': 'Serbia', 'Vantaa': 'Finland', 'Malkerns': 'Swaziland',
                     'Tarouba': 'West Indies', 'Port Vila': 'Vanuatu', 'Benoni': 'South Africa', 'Sano': 'Japan'
                     }

code_to_country = {'AUS': 'Australia', 'NZ': 'New Zealand', 'ENG': 'England', 'SA': 'South Africa', 'WI': 'West Indies',
                   'SL': 'Sri Lanka', 'PAK': 'Pakistan', 'BAN': 'Bangladesh', 'ZIM': 'Zimbabwe', 'INDIA': 'India',
                   'KENYA': 'Kenya', 'SCOT': 'Scotland', 'NED': 'Netherlands', 'IRE': 'Ireland', 'CAN': 'Canada',
                   'BMUDA': 'Bermuda', 'AFG': 'Afghanistan', 'NEPAL': 'Nepal', 'UAE': 'UAE', 'PNG': 'Papua New Guinea',
                   'OMA': 'Oman', 'BHR': 'Bahrain', 'Saudi': 'Saudi Arabia', 'Mald': 'Maldives', 'KUW': 'Kuwait',
                   'QAT': 'Qatar', 'USA': 'USA', 'PHI': 'Philippines', 'VAN': 'Vanuatu', 'MLT': 'Malta', 'ESP': 'Spain',
                   'Mex': 'Mexico', 'Blz': 'Belize', 'NGA': 'Nigeria', 'Ghana': 'Ghana', 'NAM': 'Namibia',
                   'UGA': 'Uganda', 'BOT': 'Botswana', 'ITA': 'Italy', 'JER': 'Jersey', 'GUE': 'Guernsey',
                   'NOR': 'Norway', 'DEN': 'Denmark', 'THAI': 'Thailand', 'Samoa': 'Samoa', 'Fin': 'Finland',
                   'SGP': 'Singapore', 'Caym': 'Cayman Islands', 'ROM': 'Romania', 'Aut': 'Austria', 'TKY': 'Turkey',
                   'LUX': 'Luxembourg', 'CZK-R': 'Czech Republic', 'Arg': 'Argentina', 'BRA': 'Brazil',
                   'Chile': 'Chile', 'Peru': 'Peru', 'SRB': 'Serbia', 'BUL': 'Bulgaria', 'GRC': 'Greece',
                   'PORT': 'Portugal', 'GIBR': 'Gibraltar', 'MOZ': 'Mozambique', 'MWI': 'Malawi', 'BHU': 'Bhutan',
                   'Iran': 'Iran', 'IOM': 'Isle of Man', 'Fran': 'France', 'SWE': 'Sweden', 'RWN': 'Rwanda',
                   'HUN': 'Hungary', 'EST': 'Estonia', 'CYP': 'Cyprus', 'SWA': 'Swaziland', 'LES': 'Lesotho',
                   'SEY': 'Seychelles', 'SLE': 'Sierra Leone', 'SUI': 'Switzerland', 'TAN': 'Tanzania',
                   'CAM': 'Cameroon', 'Bhm': 'Bahamas', 'ISR': 'Israel', 'CRT': 'Croatia', 'SVN': 'Slovenia',
                   'SWZ': 'Eswatini', 'Fiji': 'Fiji', 'COK': 'Cook Islands', 'JAPAN': 'Japan', 'INA': 'Indonesia',
                   'SKOR': 'South Korea', 'HKG': 'Hong Kong', 'CRC': 'Costa Rica', 'PNM': 'Panama', 'GER': 'Germany',
                   'Belg': 'Belgium', 'MAL': 'Malaysia'
                   }

# analyzes each match and extracts key data
match_nums = []
is_world_cup_match = []
dates = []
grounds = []
cities = []
countries = []
winners = []
bf = []
bf_runs = []
bf_wickets = []
bf_overs = []
bf_adjusted_run_rate = []
bs = []
bs_runs = []
bs_wickets = []
bs_overs = []
bs_adjusted_run_rate = []
num_of_matches = len(match_ids)
for match_num, match_id in enumerate(match_ids):
    match = Match(match_id)
    # 'World' or 'ICC' teams are not official national teams and matches including them are discarded
    if match.team_1_abbreviation in ['World', 'ICC'] or match.team_2_abbreviation in ['World', 'ICC']:
        continue
    match_nums.append(match_num + 1)
    dates.append(match.date)
    if 19 <= match_num <= 46:
        is_world_cup_match.append(True)
    elif 89 <= match_num <= 115:
        is_world_cup_match.append(True)
    elif 150 <= match_num <= 176:
        is_world_cup_match.append(True)
    elif 262 <= match_num <= 288:
        is_world_cup_match.append(True)
    elif 365 <= match_num <= 399:
        is_world_cup_match.append(True)
    elif 521 <= match_num <= 556:
        is_world_cup_match.append(True)
    elif match_num in wc_2021_match_nums:
        is_world_cup_match.append(True)
    else:
        is_world_cup_match.append(False)
    full_ground_name = match.ground_name
    if "," in full_ground_name:
        grounds.append(full_ground_name.split(',')[0])
    else:
        grounds.append(full_ground_name)
    cities.append(match.town_name)
    countries.append(cities_to_country[cities[-1]])
    # These matches included Brazil, but the espn.crincinfo.match did not return Brazil
    if match_id in ['1200203', '1200204', '1200207', '1200211']:
        temp_match_winner = match.match_winner
        if temp_match_winner == '':
            winners.append('Brazil')
        else:
            winners.append(code_to_country[match.match_winner])
        team_1 = match.team_1_abbreviation
        team_2 = match.team_2_abbreviation
        batting_first = match.batting_first
        if team_1 == '':
            team_1 = 'Brazil'
            team_2 = code_to_country[team_2]
        else:
            team_1 = code_to_country[team_1]
            team_2 = 'Brazil'
        if batting_first == '':
            batting_first = 'Brazil'
        else:
            batting_first = code_to_country[batting_first]
    else:
        if match.result[0:9] == 'No result':
            winners.append('No Result')
        elif match.result[0:10] == 'Match tied':
            winners.append('Tie')
        elif match.result == 'Match abandoned without a ball bowled':
            winners.append('No Result')
        else:
            winners.append(code_to_country[match.match_winner])
        team_1 = code_to_country[match.team_1_abbreviation]
        team_2 = code_to_country[match.team_2_abbreviation]
        batting_first = code_to_country[match.batting_first]
    innings = match.innings
    if len(innings) > 0:
        for inning_number, inning in enumerate(innings):
            if inning_number == 0:
                bf.append(batting_first)
                bf_runs.append(int(inning['runs']))
                bf_wickets.append(int(inning['wickets']))
                overs_completed = int(inning['balls']) // 6
                balls_in_last_over = int(inning['balls']) % 6
                overs = str(overs_completed)
                if balls_in_last_over != 0:
                    overs += '.' + str(balls_in_last_over)
                bf_overs.append(overs)
                if bf_wickets[-1] != 10:
                    balls_for_rr = overs_completed * 6 + balls_in_last_over
                else:
                    balls_for_rr = int(inning['ball_limit'])
                if balls_for_rr == 0:
                    bf_adjusted_run_rate.append('NA')
                else:
                    bf_adjusted_run_rate.append(bf_runs[-1] / balls_for_rr * 6)
            else:
                if team_1 == batting_first:
                    bs.append(team_2)
                else:
                    bs.append(team_1)
                bs_runs.append(int(inning['runs']))
                bs_wickets.append(int(inning['wickets']))
                overs_completed = int(inning['balls']) // 6
                balls_in_last_over = int(inning['balls']) % 6
                overs = str(overs_completed)
                if balls_in_last_over != 0:
                    overs += '.' + str(balls_in_last_over)
                bs_overs.append(overs)
                if bf_wickets[-1] != 10:
                    balls_for_rr = int(inning['balls'])
                else:
                    balls_for_rr = int(inning['ball_limit'])
                if balls_for_rr == 0:
                    bs_adjusted_run_rate.append('NA')
                else:
                    bs_adjusted_run_rate.append(bs_runs[-1] / balls_for_rr * 6)
    else:
        # this is for matches where a match was abandoned before a ball was bowled
        bf.append(batting_first)
        bf_runs.append(0)
        bf_wickets.append(0)
        bf_overs.append(0)
        bf_adjusted_run_rate.append('NA')
        if team_1 == batting_first:
            bs.append(team_2)
        else:
            bs.append(team_1)
        bs_runs.append(0)
        bs_wickets.append(0)
        bs_overs.append(0)
        bs_adjusted_run_rate.append('NA')
    print(str((match_num + 1) * 100 / num_of_matches) + '% complete')


# Creates a data frame to store all of the data recorded from the matches
data = {'T20I #': match_nums, 'World Cup Match?': is_world_cup_match, 'Winner': winners, 'Date': dates,
        'Batting First': bf, 'Team 1 Runs': bf_runs, 'Team 1 Wickets': bf_wickets, 'Team 1 Overs': bf_overs,
        'Team 1 Adjusted Run Rate': bf_adjusted_run_rate, 'Batting Second': bs, 'Team 2 Runs': bs_runs,
        'Team 2 Wickets': bs_wickets, 'Team 2 Overs': bs_overs,
        'Team 2 Adjusted Run Rate': bs_adjusted_run_rate, 'Ground': grounds, 'City': cities, 'Country': countries}
df = pd.DataFrame(data)
# saves data frame to a CSV file
df.to_csv("T20I_Matches_Data.csv", index=False, header=True)
