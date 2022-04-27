help:
	@echo 'How to use our repository                                                 '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                           clearing all figures/output folders        '
	@echo '   make all                              re-run all analysis folders       '
	@echo '   make env                              runs the code to download the correct packages given the notebook environment'
	@echo '                                                                          '
    
    
clean:
	rm -rf figurs
	rm -rf audio
	@echo ' Clearing Figures folder                                                                        '
	mkdir figurs
	mkdir audio
	touch figurs/.gitkeep
	touch figurs/.gitkeep
    
html:
	jupyter-book build .
	ghp-import -n -p -f _build/html 
    
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo 'Please go to https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html'
	python -m http.server



all:
	conda activate ligo
	jupyter execute index.ipynb
    
env:
	conda env create -f environment.yml
	conda activate ligo
   