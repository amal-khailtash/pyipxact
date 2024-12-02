########################################################################################################################
# Based on: https://gist.github.com/prwhite/8168133
########################################################################################################################

########################################################################################################################
# Variables (Common)
########################################################################################################################
SHELL          = /bin/bash -o pipefail

.DEFAULT_GOAL  = help
# MAKEFLAGS     += --warn-undefined-variables

UC             = $(shell echo '$1' | tr '[:lower:]' '[:upper:]')
LC             = $(shell echo '$1' | tr '[:upper:]' '[:lower:]')

# Fix for machines with bad locale setting!
export LC_ALL  = en_US.utf-8
export LANG    = en_US.utf-8

# COLORS
# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# https://linuxcommand.org/lc3_adv_tput.php
FG_BLACK      = \033[30m
FG_RED        = \033[31m
FG_GREEN      = \033[32m
FG_YELLOW     = \033[33m
FG_BLUE       = \033[34m
FG_MAGENTA    = \033[35m
FG_CYAN       = \033[36m
FG_WHITE      = \033[37m

# Bright
FG_BR_BLACK   = \033[90m
FG_BR_RED     = \033[91m
FG_BR_GREEN   = \033[92m
FG_BR_YELLOW  = \033[93m
FG_BR_BLUE    = \033[94m
FG_BR_MAGENTA = \033[95m
FG_BR_CYAN    = \033[96m
FG_BR_WHITE   = \033[97m

BG_BLACK      = \033[40m
BG_RED        = \033[41m
BG_GREEN      = \033[42m
BG_YELLOW     = \033[43m
BG_BLUE       = \033[44m
BG_MAGENTA    = \033[45m
BG_CYAN       = \033[46m
BG_WHITE      = \033[47m

# Bright
BG_BR_BLACK   = \033[100m
BG_BR_RED     = \033[101m
BG_BR_GREEN   = \033[102m
BG_BR_YELLOW  = \033[103m
BG_BR_BLUE    = \033[104m
BG_BR_MAGENTA = \033[105m
BG_BR_CYAN    = \033[106m
BG_BR_WHITE   = \033[107m

RESET         = \033[0m
BOLD          = \033[1m
DIM           = \033[2m
ITALIC        = \033[3m
UNDERLINE     = \033[4m
BLINK_SLOW    = \033[5m
BLINK_FAST    = \033[6m
REVERSED      = \033[7m
CROSSED       = \033[9m

BOLD_OFF      = \033[21m
DIM_OFF       = \033[22m
ITALIC_OFF    = \033[23m
UNDERLINE_OFF = \033[24m
BLINK_OFF     = \033[25m
REVERSED_OFF  = \033[27m
CROSSED_OFF   = \033[29m

PASS          = ✅
FAIL          = ❌

# ----------------------------------------------------------------------------------------------------------------------
# help: ## Show this help message
# ----------------------------------------------------------------------------------------------------------------------
.PHONY: help
help:
	@echo   "     ___           ___                         ___    "
	@echo   "    /__/\         /  /\                       /  /\   "
	@echo   "    \  \:\       /  /:/_                     /  /::\  "
	@echo   "     \__\:\     /  /:/ /\    ___     ___    /  /:/\:\ "
	@echo   " ___ /  /::\   /  /:/ /:/_  /__/\   /  /\  /  /:/~/:/ "
	@echo   "/__/\  /:/\:\ /__/:/ /:/ /\ \  \:\ /  /:/ /__/:/ /:/  "
	@echo   "\  \:\/:/__\/ \  \:\/:/ /:/  \  \:\  /:/  \  \:\/:/   "
	@echo   " \  \::/       \  \::/ /:/    \  \:\/:/    \  \::/    "
	@echo   "  \  \:\        \  \:\/:/      \  \::/      \  \:\    "
	@echo   "   \  \:\        \  \::/        \__\/        \  \:\   "
	@echo   "    \__\/         \__\/                       \__\/   "
	@printf "\n"
	@printf "${BOLD}Usage:${RESET}\n"
	@printf "  make ${FG_CYAN}<target>${RESET}\n"
	@printf "  make ${FG_CYAN}<target> ${FG_YELLOW}[<VAR1>=<value1>] [<VAR2>=<value2>]${RESET} ...\n"
#	@printf "\n"
#	@printf "${BOLD}Targets:${RESET}\n"
	@awk \
		'BEGIN {FS = ":.*##";} \
		/^# .*?:.*?##/ { \
			TARGET=substr($$1, 2); \
			DESCRIPTION=$$2; \
			gsub(/^ */, "", TARGET); \
			printf "  ${FG_CYAN}%-37s${RESET}- ${FG_GREEN}%s${RESET}\n", TARGET, DESCRIPTION \
		} \
		/^##@/ { \
			LEN=length(substr($$0, 5)); \
			printf "\n${BOLD}%s\n%.*s${RESET}\n", substr($$0, 5), LEN, "=================================================="; \
		}' $(MAKEFILE_LIST)
