.PHONY: test test-cov

TAG="\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

test:
	@echo $(TAG)Running tests$(END)
	py.test quiz-questions/*.py --tb=short -v
