prepare_stage1:
	poetry run python C:/Users/go130/dvc_example/data/data_download.py

prepare_stage2:
	poetry run python C:/Users/go130/dvc_example/data/data_prepare.py

data_prepare: prepare_stage1 prepare_stage2
