PANDOC ?= pandoc
PANDOC_FLAGS = --smart

# R Markdown files.
SRC_RMD = $(wildcard ??-*.Rmd)
DST_RMD = $(patsubst %.Rmd,%.md,$(SRC_RMD))

# All Markdown files (hand-written and generated).
ALL_MD = $(wildcard *.md) $(DST_RMD)
EXCLUDE_MD = README.md 
SRC_MD = $(filter-out $(EXCLUDE_MD),$(ALL_MD))
DST_HTML = $(patsubst %.md,%.html,$(SRC_MD))

# All outputs.
DST_ALL = $(DST_HTML)

# Pandoc filters.
FILTERS = $(wildcard tools/filters/*.py)

# Inclusions.
#INCLUDES = \
	-Vheader="$$(cat _includes/header.html)" \
	-Vbanner="$$(cat _includes/banner.html)" \
	-Vfooter="$$(cat _includes/footer.html)" \
	-Vjavascript="$$(cat _includes/javascript.html)"

# Default action is to show what commands are available.
all : commands

## check    : Validate all lesson content against the template.
check: $(ALL_MD)

## clean    : Clean up temporary and intermediate files.
clean :
	@rm -rf $$(find . -name '*~' -print)
	@rm -rf $(DST_HTML)

## preview  : Build website locally for checking.
preview : $(DST_ALL)

# Pattern to build a generic page.
%.html : %.md $(FILTERS)
	${PANDOC} -s -t html \
	    ${PANDOC_FLAGS} \
	    $(INCLUDES) \
	    -o $@ $<

## commands : Display available commands.
commands : Makefile
	@sed -n 's/^##//p' $<

## settings : Show variables and settings.
settings :
	@echo 'PANDOC:' $(PANDOC)
	@echo 'SRC_RMD:' $(SRC_RMD)
	@echo 'DST_RMD:' $(DST_RMD)
	@echo 'SRC_MD:' $(SRC_MD)
	@echo 'DST_HTML:' $(DST_HTML)

