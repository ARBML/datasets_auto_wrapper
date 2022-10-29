import os
import pandas as pd 
import datasets

class COVID_FAES_ar(datasets.GeneratorBasedBuilder):
	def _info(self):
		return datasets.DatasetInfo(features=datasets.Features({'id':datasets.Value('string'),'ft0':datasets.Value('string'),'ft1':datasets.Value('string'),'ft2':datasets.Value('string'),'ft3':datasets.Value('string'),'ft4':datasets.Value('string'),'ft5':datasets.Value('string'),'ft6':datasets.Value('string'),'ft7':datasets.Value('string'),'ft8':datasets.Value('string'),'ft9':datasets.Value('string'),'ft10':datasets.Value('string'),'ft11':datasets.Value('string'),'ft12':datasets.Value('string'),'ft13':datasets.Value('string'),'ft14':datasets.Value('string'),'ft15':datasets.Value('string'),'ft16':datasets.Value('string'),'ft17':datasets.Value('string'),'ft18':datasets.Value('string'),'ft19':datasets.Value('string'),'ft20':datasets.Value('string'),'ft21':datasets.Value('string'),'ft22':datasets.Value('string'),'ft23':datasets.Value('string'),'ft24':datasets.Value('string'),'ft25':datasets.Value('string'),'ft26':datasets.Value('string'),'ft27':datasets.Value('string'),'ft28':datasets.Value('string'),'ft29':datasets.Value('string'),'ft30':datasets.Value('string'),'ft31':datasets.Value('string'),'ft32':datasets.Value('string'),'ft33':datasets.Value('string'),'ft34':datasets.Value('string'),'ft35':datasets.Value('string'),'ft36':datasets.Value('string'),'ft37':datasets.Value('string'),'ft38':datasets.Value('string'),'ft39':datasets.Value('string'),'ft40':datasets.Value('string'),'ft41':datasets.Value('string'),'ft42':datasets.Value('string'),'ft43':datasets.Value('string'),'ft44':datasets.Value('string'),'ft45':datasets.Value('string'),'ft46':datasets.Value('string'),'ft47':datasets.Value('string'),'ft48':datasets.Value('string'),'ft49':datasets.Value('string'),'ft50':datasets.Value('string'),'ft51':datasets.Value('string'),'ft52':datasets.Value('string'),'ft53':datasets.Value('string'),'ft54':datasets.Value('string'),'ft55':datasets.Value('string'),'ft56':datasets.Value('string'),'ft57':datasets.Value('string'),'ft58':datasets.Value('string'),'ft59':datasets.Value('string'),'ft60':datasets.Value('string'),'ft61':datasets.Value('string'),'ft62':datasets.Value('string'),'ft63':datasets.Value('string'),'ft64':datasets.Value('string'),'ft65':datasets.Value('string'),'ft66':datasets.Value('string'),'ft67':datasets.Value('string'),'ft68':datasets.Value('string'),'ft69':datasets.Value('string'),'ft70':datasets.Value('string'),'ft71':datasets.Value('string'),'ft72':datasets.Value('string'),'ft73':datasets.Value('string'),'ft74':datasets.Value('string'),'ft75':datasets.Value('string'),'ft76':datasets.Value('string'),'ft77':datasets.Value('string'),'ft78':datasets.Value('string'),'ft79':datasets.Value('string'),'ft80':datasets.Value('string'),'ft81':datasets.Value('string'),'ft82':datasets.Value('string'),'ft83':datasets.Value('string'),'ft84':datasets.Value('string'),'ft85':datasets.Value('string'),'ft86':datasets.Value('string'),'ft87':datasets.Value('string'),'ft88':datasets.Value('string'),'ft89':datasets.Value('string'),'ft90':datasets.Value('string'),'ft91':datasets.Value('string')}))
	def _split_generators(self, dl_manager):
		url = ['https://github.com/mohaddad/COVID-FAKES/archive/COVID-FAKES-A.zip']
		downloaded_files = dl_manager.download_and_extract(url)
		return [datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'filepaths': [os.path.join(downloaded_files[0],f) for f in ['COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_7.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_14.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_4.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_5.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_19.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_21.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_9.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_16.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_2.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_6.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_22.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_3.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_1.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_20.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_13.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_17.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_10.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_15.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_8.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_18.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_11.csv', 'COVID-FAKES-COVID-FAKES-A/Arabic_Final_Annotation_results_12.csv']]})]
	def _generate_examples(self, filepaths):
		_id = 0
		labels = None
		for i,filepath in enumerate(filepaths):
			df = pd.read_csv(open(filepath, 'rb'), sep = ';', skiprows = 0, error_bad_lines = False, header = None, engine = 'python')
			df.columns = ['id', 'ft0', 'ft1', 'ft2', 'ft3', 'ft4', 'ft5', 'ft6', 'ft7', 'ft8', 'ft9', 'ft10', 'ft11', 'ft12', 'ft13', 'ft14', 'ft15', 'ft16', 'ft17', 'ft18', 'ft19', 'ft20', 'ft21', 'ft22', 'ft23', 'ft24', 'ft25', 'ft26', 'ft27', 'ft28', 'ft29', 'ft30', 'ft31', 'ft32', 'ft33', 'ft34', 'ft35', 'ft36', 'ft37', 'ft38', 'ft39', 'ft40', 'ft41', 'ft42', 'ft43', 'ft44', 'ft45', 'ft46', 'ft47', 'ft48', 'ft49', 'ft50', 'ft51', 'ft52', 'ft53', 'ft54', 'ft55', 'ft56', 'ft57', 'ft58', 'ft59', 'ft60', 'ft61', 'ft62', 'ft63', 'ft64', 'ft65', 'ft66', 'ft67', 'ft68', 'ft69', 'ft70', 'ft71', 'ft72', 'ft73', 'ft74', 'ft75', 'ft76', 'ft77', 'ft78', 'ft79', 'ft80', 'ft81', 'ft82', 'ft83', 'ft84', 'ft85', 'ft86', 'ft87', 'ft88', 'ft89', 'ft90', 'ft91']
			for _, record in df.iterrows():
				yield str(_id), {'id':record['id'],'ft0':record['ft0'],'ft1':record['ft1'],'ft2':record['ft2'],'ft3':record['ft3'],'ft4':record['ft4'],'ft5':record['ft5'],'ft6':record['ft6'],'ft7':record['ft7'],'ft8':record['ft8'],'ft9':record['ft9'],'ft10':record['ft10'],'ft11':record['ft11'],'ft12':record['ft12'],'ft13':record['ft13'],'ft14':record['ft14'],'ft15':record['ft15'],'ft16':record['ft16'],'ft17':record['ft17'],'ft18':record['ft18'],'ft19':record['ft19'],'ft20':record['ft20'],'ft21':record['ft21'],'ft22':record['ft22'],'ft23':record['ft23'],'ft24':record['ft24'],'ft25':record['ft25'],'ft26':record['ft26'],'ft27':record['ft27'],'ft28':record['ft28'],'ft29':record['ft29'],'ft30':record['ft30'],'ft31':record['ft31'],'ft32':record['ft32'],'ft33':record['ft33'],'ft34':record['ft34'],'ft35':record['ft35'],'ft36':record['ft36'],'ft37':record['ft37'],'ft38':record['ft38'],'ft39':record['ft39'],'ft40':record['ft40'],'ft41':record['ft41'],'ft42':record['ft42'],'ft43':record['ft43'],'ft44':record['ft44'],'ft45':record['ft45'],'ft46':record['ft46'],'ft47':record['ft47'],'ft48':record['ft48'],'ft49':record['ft49'],'ft50':record['ft50'],'ft51':record['ft51'],'ft52':record['ft52'],'ft53':record['ft53'],'ft54':record['ft54'],'ft55':record['ft55'],'ft56':record['ft56'],'ft57':record['ft57'],'ft58':record['ft58'],'ft59':record['ft59'],'ft60':record['ft60'],'ft61':record['ft61'],'ft62':record['ft62'],'ft63':record['ft63'],'ft64':record['ft64'],'ft65':record['ft65'],'ft66':record['ft66'],'ft67':record['ft67'],'ft68':record['ft68'],'ft69':record['ft69'],'ft70':record['ft70'],'ft71':record['ft71'],'ft72':record['ft72'],'ft73':record['ft73'],'ft74':record['ft74'],'ft75':record['ft75'],'ft76':record['ft76'],'ft77':record['ft77'],'ft78':record['ft78'],'ft79':record['ft79'],'ft80':record['ft80'],'ft81':record['ft81'],'ft82':record['ft82'],'ft83':record['ft83'],'ft84':record['ft84'],'ft85':record['ft85'],'ft86':record['ft86'],'ft87':record['ft87'],'ft88':record['ft88'],'ft89':record['ft89'],'ft90':record['ft90'],'ft91':record['ft91']}
				_id += 1 
