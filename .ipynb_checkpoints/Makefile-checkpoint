help:
	@echo 'How to use our repository                                                 '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                         clearing all figures/output folders        '
	@echo '   make all                           re-run all analysis folders       '
	@echo '   make env                           runs the code to download the correct packages given the notebook environment'
	@echo '   make html                          builds the website'
	@echo '   make book                          builds the website, downloads the correct packages and switches environments'
	@echo '   make html-hub                      makes website viewable in the hub'
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
	conda activate jupyterbook
	jupyter-book build .
	ghp-import -n -p -f _build/html 
    
html-hub:
	conda activate jupyterbook
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo 'Please go to https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html'
	python -m http.server

book:
	conda create -n jupyterbook 
	conda activate jupyterbook
	conda install -c conda-forge jupyter-book
	make html

all:
	conda activate ligo
	jupyter execute index.ipynb
    
env:
	conda env create -f environment.yml
	conda activate ligo
   