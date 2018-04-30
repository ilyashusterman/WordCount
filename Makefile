################################################################################
# Makefile for installing plugins , setting database
################################################################################

# Prefer bash shell
export SHELL=/bin/bash

self := $(abspath $(lastword $(MAKEFILE_LIST)))
parent := $(dir $(self))

ifneq (,$(VERBOSE))
    override VERBOSE:=
else
    override VERBOSE:=@
endif

#--database=sqlite3

.PHONY: create_local_db
create_local_db:
	$(VERBOSE) echo "Creating database..."
	$(VERBOSE) sqlite3 word_count_machine/wordcount_users.db <<< "CREATE TABLE IF NOT EXISTS \`wordcount_users\` (\`username\` VARCHAR(25) UNIQUE NOT NULL, \`password\` VARCHAR(25) NOT NULL);"
	$(VERBOSE) sqlite3 word_count_machine/wordcount_users.db <<< "INSERT INTO \`wordcount_users\` VALUES('ilya', 'password');"
	$(VERBOSE) echo "Created wordcount_users successfully"
.PHONY: db_drop_local
db_drop_local:
	$(VERBOSE) echo "Dropping local wordcount db file"
	-$(VERBOSE) rm -rf word_count_machine/wordcount_users.db
.PHONY: test
test:
	$(VERBOSE) nosetests -sv --collect-only