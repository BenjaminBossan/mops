test_no_matching:
	python -m pytest mops/ -k "this-does-not-match-any-test" $(if $(IS_GITHUB_CI),--report-log "some.log",)
