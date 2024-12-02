########################################################################################################################
########################################################################################################################
SHELL        := /bin/bash

MAKEFILE_DIR  = $(patsubst %/,%,$(dir $(realpath $(firstword $(MAKEFILE_LIST)))))

-include $(MAKEFILE_DIR)/Makefile-helper.mk

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UV:=$(shell uv --version)
ifdef UV
        VENV := uv venv
        PIP  := uv pip
else
        VENV := python -m venv
        PIP  := python -m pip
endif

run     := uv run
python  := $(run) python
lint    := $(run) pylint
test    := $(run) pytest
pyright := $(run) pyright
black   := $(run) black
ruff    := $(run) ruff


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##@ Setup:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----------------------------------------------------------------------------------------------------------------------
# setup-submodules: ## Fetch all submodules needed for this project
# ----------------------------------------------------------------------------------------------------------------------
.PHONY: setup-submodules
setup-submodules:
	@git submodule update --init --recursive
	@( \
		cd submodules/accellera-schemas/ ; \
		git checkout v1.0.0              ; \
	)


# ----------------------------------------------------------------------------------------------------------------------
# uv: ## Install uv
# ----------------------------------------------------------------------------------------------------------------------
.PHONY: uv
uv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh


# ----------------------------------------------------------------------------------------------------------------------
# venv: ## Create a virtual environment
# ----------------------------------------------------------------------------------------------------------------------
.venv:
	$(VENV) .venv

venv: .venv
	@echo "run 'source .venv/bin/activate' to use virtualenv"


# ----------------------------------------------------------------------------------------------------------------------
# uv-sync: ## Sync the project's dependencies with the environment.
# ----------------------------------------------------------------------------------------------------------------------
.PHONY: uv-sync
uv-sync:
	uv sync


# ----------------------------------------------------------------------------------------------------------------------
# uv-lock: ## Create a lockfile for the project's dependencies.
# ----------------------------------------------------------------------------------------------------------------------
.PHONY: uv-lock
uv-lock:
	uv lock


# ----------------------------------------------------------------------------------------------------------------------
# generate-bindings: ## Generate Python bindings using xsdata
# ----------------------------------------------------------------------------------------------------------------------
# XSDATA_STRUCTURE_STYLE := namespaces
# XSDATA_STRUCTURE_STYLE := single-package
  XSDATA_STRUCTURE_STYLE := clusters
# XSDATA_STRUCTURE_STYLE := filenames

  XSDATA_OPTIONS :=
  XSDATA_OPTIONS += --slots
# XSDATA_OPTIONS += --kw-only
# XSDATA_OPTIONS += --union-type
# XSDATA_OPTIONS += --compound-fields
# XSDATA_OPTIONS += --wrapper-fields
  XSDATA_OPTIONS += --subscriptable-types
  XSDATA_OPTIONS += --generic-collections
# XSDATA_OPTIONS += --relative-imports
  XSDATA_OPTIONS += --structure-style $(XSDATA_STRUCTURE_STYLE)
# XSDATA_OPTIONS += --unnest-classes

  # XML_SCHEMAS_ROOT := http://www.accellera.org/XMLSchema
  XML_SCHEMAS_ROOT := ../submodules/accellera-schemas

generate-bindings:
	@rm -rf src/org
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1.0 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_0                 $(XML_SCHEMAS_ROOT)/SPIRIT/1.0/index.xsd)
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1.1 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_1                 $(XML_SCHEMAS_ROOT)/SPIRIT/1.1/index.xsd)
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1.2 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_2                 $(XML_SCHEMAS_ROOT)/SPIRIT/1.2/index.xsd)
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1.4 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_4                 $(XML_SCHEMAS_ROOT)/SPIRIT/1.4/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_4.tgi             $(XML_SCHEMAS_ROOT)/SPIRIT/1.4/TGI/TGI.wsdl)
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1.5 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_5                 $(XML_SCHEMAS_ROOT)/SPIRIT/1.5/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1_5.tgi             $(XML_SCHEMAS_ROOT)/SPIRIT/1.5/TGI/TGI.wsdl)
#
	@echo "========================================================================================================================"
	@echo "Generating SPIRIT/1685-2009 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009           $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.tgi       $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009/TGI/TGI.wsdl)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.ve        $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009-VE-1.0/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.ve.ams    $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009-VE-1.0/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.ve.core   $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009-VE-1.0/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.ve.pdp    $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009-VE-1.0/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.spirit.v1685_2009.ve.power  $(XML_SCHEMAS_ROOT)/SPIRIT/1685-2009-VE-1.0/index.xsd)
#
	@echo "========================================================================================================================"
	@echo "Generating IPXACT/1685-2014 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.ipxact.v1685_2014           $(XML_SCHEMAS_ROOT)/IPXACT/1685-2014/index.xsd)
#
	@echo "========================================================================================================================"
	@echo "Generating IPXACT/1685-2022 bindings..."
	@echo "========================================================================================================================"
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.ipxact.v1685_2022           $(XML_SCHEMAS_ROOT)/IPXACT/1685-2022/index.xsd)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.ipxact.v1685_2022.tgi       $(XML_SCHEMAS_ROOT)/IPXACT/1685-2022/TGI/TGI.wsdl)
	(cd src; xsdata generate $(XSDATA_OPTIONS) --package org.accellera.ipxact.v1685_2022.ve        $(XML_SCHEMAS_ROOT)/IPXACT/1685-2022-VE-1.0/index.xsd)
