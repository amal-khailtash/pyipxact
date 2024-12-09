<!--
  Licensed to Accellera Systems Initiative Inc. (Accellera) under one or
  more contributor license agreements.  See the NOTICE file distributed
  with this work for additional information regarding copyright ownership.
  Accellera licenses this file to you under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with the
  License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
  implied.  See the License for the specific language governing
  permissions and limitations under the License.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ipxact2014="http://www.accellera.org/XMLSchema/IPXACT/1685-2014" xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2022" version="1.0" xmlns:xalan="http://xml.apache.org/xalan" xmlns:exslt="http://exslt.org/common" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="xalan exslt msxsl ipxact2014">
	<xsl:strip-space elements="*"/>
	<xsl:output method="xml" indent="yes"/>
	<xsl:param name="verbose" select="true()"/>
	<xsl:param name="namespace" select="'http://www.accellera.org/XMLSchema/IPXACT/1685-2022'"/>
	<xsl:param name="VE.namespace" select="'http://www.accellera.org/XMLSchema/IPXACT/1685-2022-VE'"/>
	<xsl:param name="COND.namespace" select="'http://www.accellera.org/XMLSchema/IPXACT/1685-2022-VE/COND-1.0'"/>
	<xsl:param name="prefix" select="true()"/>
	<!-- Process the document node. -->
	<xsl:template match="/">
		<xsl:apply-templates select="comment() | processing-instruction()"/>
		<xsl:apply-templates select="*"/>
	</xsl:template>
	<xsl:template match="*">
		<xsl:element name="{name()}" namespace="{namespace-uri()}">
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</xsl:element>
	</xsl:template>
	<!-- Copy comments, pi's and text. -->
	<xsl:template match="comment() | processing-instruction()">
		<xsl:copy>
			<xsl:apply-templates/>
		</xsl:copy>
		<xsl:text>
</xsl:text>
	</xsl:template>
	
	<xsl:template name="insertComment">
		<xsl:param name="number"/>
		<xsl:param name="message"/>
		<xsl:if test="$verbose">
			<xsl:message>IP-XACT 1685-2022 XSLT Warning#<xsl:value-of select="$number"/>: <xsl:value-of select="$message"/>
			</xsl:message>
		</xsl:if>
		<xsl:comment> IP-XACT 1685-2022 XSLT Warning#<xsl:value-of select="$number"/>: <xsl:value-of select="$message"/>
		</xsl:comment>
	</xsl:template>
	
	<xsl:template match="@*">
		<xsl:attribute name="{name()}" namespace="{namespace-uri()}"><xsl:value-of select="."/></xsl:attribute>
	</xsl:template>
	
	<xsl:template match="/ipxact2014:*">
		<xsl:element name="ipxact:{local-name()}" namespace="{$namespace}">
			<xsl:for-each select="namespace::*">
				<xsl:if test="not(.='http://www.accellera.org/XMLSchema/IPXACT/1685-2014')">
					<xsl:copy/>
				</xsl:if>
			</xsl:for-each>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</xsl:element>
	</xsl:template>
	
	<xsl:template match="@usageType">
		<xsl:variable name="language" select="translate(../../../ipxact2014:language, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"/>
		<xsl:choose>
			<xsl:when test="$language = 'vhdl' or $language = 'verilog'">
				<xsl:attribute name="usageType">typed</xsl:attribute>
			</xsl:when>
			<xsl:otherwise>
				<xsl:attribute name="usageType"><xsl:value-of select="."/></xsl:attribute>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	<xsl:template match="ipxact2014:moduleParameter">
		<ipxact:moduleParameter>
			<xsl:apply-templates select="@*"/>
			<xsl:if test="not(@usageType)">
				<xsl:variable name="language" select="translate(../../ipxact2014:language, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"/>
				<xsl:choose>
					<xsl:when test="$language = 'vhdl' or $language = 'verilog'">
						<xsl:attribute name="usageType">typed</xsl:attribute>
					</xsl:when>
					<xsl:otherwise>
						<xsl:attribute name="usageType">nontyped</xsl:attribute>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
			<xsl:apply-templates select="*"/>

			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:moduleParameter>
	</xsl:template>
	
	
	<xsl:template match="@xsi:schemaLocation">
		<xsl:attribute name="xsi:schemaLocation"><xsl:text>http://www.accellera.org/XMLSchema/IPXACT/1685-2022 http://www.accellera.org/XMLSchema/IPXACT/1685-2022/index.xsd</xsl:text></xsl:attribute>
	</xsl:template>
	
	<xsl:template match="ipxact2014:*">
		<xsl:element name="ipxact:{local-name()}" namespace="{$namespace}">
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</xsl:element>
	</xsl:template>

	<xsl:template match="/ipxact2014:component" priority="1">
		<xsl:element name="ipxact:{local-name()}" namespace="{$namespace}">
			<xsl:for-each select="namespace::*">
				<xsl:if test="not(.='http://www.accellera.org/XMLSchema/IPXACT/1685-2014')">
					<xsl:copy/>
				</xsl:if>
			</xsl:for-each>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates select="ipxact2014:vendor"/>
			<xsl:apply-templates select="ipxact2014:library"/>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:version"/>
			<xsl:apply-templates select="ipxact2014:busInterfaces"/>
			<xsl:apply-templates select="ipxact2014:indirectInterfaces"/>
			<xsl:apply-templates select="ipxact2014:channels"/>
			<xsl:if test="not(ipxact2014:remapStates) and (ipxact2014:resetTypes/ipxact2014:resetType | .//ipxact2014:register/ipxact2014:alternateRegisters/ipxact2014:alternateRegister/ipxact2014:alternateGroups/ipxact2014:alternateGroup)">
				<ipxact:modes>
					<xsl:for-each select="ipxact2014:resetTypes/ipxact2014:resetType">
						<ipxact:mode>
							<ipxact:name>resetType_<xsl:value-of select="ipxact2014:name"/></ipxact:name>
							<xsl:apply-templates select="ipxact2014:displayName"/>
							<xsl:apply-templates select="ipxact2014:description"/>
							<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
							<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
								<xsl:call-template name="convertIsPresent"/>
							</xsl:if>
						</ipxact:mode>
					</xsl:for-each>
					<xsl:for-each select=".//ipxact2014:register/ipxact2014:alternateRegisters/ipxact2014:alternateRegister/ipxact2014:alternateGroups/ipxact2014:alternateGroup[not(.=preceding::*)]">
						<ipxact:mode>
							<ipxact:name>alternateGroup_<xsl:value-of select="."/></ipxact:name>
						</ipxact:mode>
					</xsl:for-each>
				</ipxact:modes>
			</xsl:if>
			<xsl:apply-templates select="ipxact2014:remapStates"/>
			<xsl:apply-templates select="ipxact2014:addressSpaces"/>
			<xsl:apply-templates select="ipxact2014:memoryMaps"/>
			<xsl:apply-templates select="ipxact2014:model"/>
			<xsl:apply-templates select="ipxact2014:componentGenerators"/>
			<xsl:apply-templates select="ipxact2014:choices"/>
			<xsl:apply-templates select="ipxact2014:fileSets"/>
			<xsl:apply-templates select="ipxact2014:whiteboxElements"/>
			<xsl:apply-templates select="ipxact2014:cpus"/>
			<xsl:apply-templates select="ipxact2014:otherClockDrivers"/>
			<xsl:apply-templates select="ipxact2014:resetTypes"/>
			<xsl:apply-templates select="ipxact2014:parameters"/>
			<xsl:apply-templates select="ipxact2014:assertions"/>
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
		</xsl:element>
	</xsl:template>

	<xsl:template match="/ipxact2014:generatorChain" priority="1">
		<xsl:element name="ipxact:{local-name()}" namespace="{$namespace}">
			<xsl:for-each select="namespace::*">
				<xsl:if test="not(.='http://www.accellera.org/XMLSchema/IPXACT/1685-2014')">
					<xsl:copy/>
				</xsl:if>
			</xsl:for-each>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates select="ipxact2014:vendor"/>
			<xsl:apply-templates select="ipxact2014:library"/>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:version"/>
			<!-- displayName and description handled elsewhere -->
			<xsl:apply-templates select="ipxact2014:generatorChainSelector | ipxact2014:componentGeneratorSelector | ipxact2014:generator"/>
			<xsl:apply-templates select="ipxact2014:chainGroup"/>
			<xsl:apply-templates select="ipxact2014:choices"/>
			<xsl:apply-templates select="ipxact2014:parameters"/>
			<xsl:apply-templates select="ipxact2014:assertions"/>
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
		</xsl:element>
	</xsl:template>
	
	<!-- Move ipxact:description and ipxact:displayName -->
	<xsl:template match="/ipxact2014:*/ipxact2014:version">
		<ipxact:version><xsl:value-of select="."/></ipxact:version>
		<xsl:if test="../ipxact2014:displayName">
			<ipxact:displayName><xsl:value-of select="../ipxact2014:displayName"/></ipxact:displayName>
		</xsl:if>
		<xsl:if test="../ipxact2014:description">
			<ipxact:description><xsl:value-of select="../ipxact2014:description"/></ipxact:description>
		</xsl:if>
	</xsl:template>

	
	<xsl:template match="/ipxact2014:*/ipxact2014:description"/>
	<xsl:template match="/ipxact2014:*/ipxact2014:diplayName"/>

	<!-- Convert Master -> Initiator -->
	<xsl:template match="ipxact2014:onMaster">
		<ipxact:onInitiator>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:onInitiator>
	</xsl:template>

	<xsl:template match="ipxact2014:master">
		<ipxact:initiator>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:initiator>
	</xsl:template>

	<xsl:template match="@masterRef">
		<xsl:attribute name="initiatorRef"><xsl:value-of select="."/></xsl:attribute>
	</xsl:template>

	<xsl:template match="ipxact2014:maxMasters">
		<ipxact:maxInitiators>
			<xsl:value-of select="."/>
		</ipxact:maxInitiators>
	</xsl:template>

	<xsl:template match="ipxact2014:mirroredMaster">
		<ipxact:mirroredInitiator>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:mirroredInitiator>
	</xsl:template>

	<!-- Convert Slave -> Target -->

	<xsl:template match="ipxact2014:slave">
		<ipxact:target>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:target>
	</xsl:template>

	<xsl:template match="ipxact2014:mirroredSlave">
		<ipxact:mirroredTarget>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:mirroredTarget>
	</xsl:template>

	<xsl:template match="ipxact2014:onSlave">
		<ipxact:onTarget>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:onTarget>
	</xsl:template>

	<xsl:template match="ipxact2014:maxSlaves">
		<ipxact:maxTargets>
			<xsl:value-of select="."/>
		</ipxact:maxTargets>
	</xsl:template>
	
	<xsl:template match="ipxact2014:file/ipxact2014:fileType">
		<ipxact:fileType>
			<xsl:choose>
				<xsl:when test="@user='cSource'">cSource</xsl:when>
				<xsl:when test="@user='cppSource'">cppSource</xsl:when>
				<xsl:when test="@user='asmSource'">asmSource</xsl:when>
				<xsl:when test="@user='vhdlSource'">vhdlSource</xsl:when>
				<xsl:when test="@user='vhdlSource-87'">vhdlSource-87</xsl:when>
				<xsl:when test="@user='vhdlSource-93'">vhdlSource-93</xsl:when>
				<xsl:when test="@user='vhdlSource-2002'">vhdlSource-2002</xsl:when>
				<xsl:when test="@user='vhdlSource-2008'">vhdlSource-2008</xsl:when>
				<xsl:when test="@user='verilogSource'">verilogSource</xsl:when>
				<xsl:when test="@user='verilogSource-95'">verilogSource-95</xsl:when>
				<xsl:when test="@user='verilogSource-2001'">verilogSource-2001</xsl:when>
				<xsl:when test="@user='verilogSource-2005'">verilogSource-2005</xsl:when>
				<xsl:when test="@user='swObject'">swObject</xsl:when>
				<xsl:when test="@user='swObjectLibrary'">swObjectLibrary</xsl:when>
				<xsl:when test="@user='vhdlBinaryLibrary'">vhdlBinaryLibrary</xsl:when>
				<xsl:when test="@user='verilogBinaryLibrary'">verilogBinaryLibrary</xsl:when>
				<xsl:when test="@user='unelaboratedHdl'">unelaboratedHdl</xsl:when>
				<xsl:when test="@user='executableHdl'">executableHdl</xsl:when>
				<xsl:when test="@user='swObjectLibrary'">swObjectLibrary</xsl:when>
				<xsl:when test="@user='systemVerilogSource-3.0'">systemVerilogSource-3.0</xsl:when>
				<xsl:when test="@user='systemVerilogSource-3.1'">systemVerilogSource-3.1</xsl:when>
				<xsl:when test="@user='systemVerilogSource-3.1a'">systemVerilogSource-3.1a</xsl:when>
				<xsl:when test="@user='systemVerilogSource-2009'">systemVerilogSource-2009</xsl:when>
				<xsl:when test="@user='systemVerilogSource-2012'">systemVerilogSource-2012</xsl:when>
				<xsl:when test="@user='systemVerilogSource-2017'">systemVerilogSource-2017</xsl:when>
				<xsl:when test="@user='systemCSource'">systemCSource</xsl:when>
				<xsl:when test="@user='systemCSource-2.0'">systemCSource-2.0</xsl:when>
				<xsl:when test="@user='systemCSource-2.0.1'">systemCSource-2.0.1</xsl:when>
				<xsl:when test="@user='systemCSource-2.1'">systemCSource-2.1</xsl:when>
				<xsl:when test="@user='systemCSource-2.2'">systemCSource-2.2</xsl:when>
				<xsl:when test="@user='systemCSource-2.3'">systemCSource-2.3</xsl:when>
				<xsl:when test="@user='systemCBinaryLibrary'">systemCBinaryLibrary</xsl:when>
				<xsl:when test="@user='veraSource'">veraSource</xsl:when>
				<xsl:when test="@user='eSource'">eSource</xsl:when>
				<xsl:when test="@user='perlSource'">perlSource</xsl:when>
				<xsl:when test="@user='tclSource'">tclSource</xsl:when>
				<xsl:when test="@user='OVASource'">OVASource</xsl:when>
				<xsl:when test="@user='SVASource'">SVASource</xsl:when>
				<xsl:when test="@user='pslSource'">pslSource</xsl:when>
				<xsl:when test="@user='SDC'">SDC</xsl:when>
				<xsl:when test="@user='vhdlAmsSource'">vhdlAmsSource</xsl:when>
				<xsl:when test="@user='verilogAmsSource'">verilogAmsSource</xsl:when>
				<xsl:when test="@user='systemCAmsSource'">systemCAmsSource</xsl:when>
				<xsl:when test="@user='libertySource'">libertySource</xsl:when>
				<xsl:when test="@user='spiceSource'">spiceSource</xsl:when>
				<xsl:when test="@user='systemRDL'">systemRDL</xsl:when>
				<xsl:when test="@user='systemRDL-1.0'">systemRDL-1.0</xsl:when>
				<xsl:when test="@user='systemRDL-2.0'">systemRDL-2.0</xsl:when>
				<xsl:otherwise>
					<xsl:apply-templates select="@*"/>
					<xsl:apply-templates select="./text()"/>
				</xsl:otherwise>
			</xsl:choose>
		</ipxact:fileType>
	</xsl:template>

	<xsl:template match="ipxact2014:abstractorMode">
		<ipxact:abstractorMode>
			<xsl:choose>
				<xsl:when test=".='master'">initiator</xsl:when>
				<xsl:when test=".='mirroredMaster'">mirroredInitiator</xsl:when>
				<xsl:when test=".='slave'">target</xsl:when>
				<xsl:when test=".='mirroredSlave'">mirroredTarget</xsl:when>
				<xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
			</xsl:choose>
		</ipxact:abstractorMode>
	</xsl:template>

	<xsl:template match="@interfaceMode">
		<xsl:attribute name="interfaceMode">
			<xsl:choose>
				<xsl:when test=".='master'">initiator</xsl:when>
				<xsl:when test=".='mirroredMaster'">mirroredInitiator</xsl:when>
				<xsl:when test=".='slave'">target</xsl:when>
				<xsl:when test=".='mirroredSlave'">mirroredTarget</xsl:when>
				<xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
			</xsl:choose>
		</xsl:attribute>
	</xsl:template>
	
	<xsl:template match="ipxact2014:indirectAddressRef">
		<xsl:variable name="reference"><xsl:value-of select="."/></xsl:variable>
		<ipxact:indirectAddressRef>
			<xsl:apply-templates select="//ipxact2014:field[@fieldID=$reference]" mode="generateFieldReferenceGroup"/>
		</ipxact:indirectAddressRef>
	</xsl:template>

	<xsl:template match="ipxact2014:indirectDataRef">
		<xsl:variable name="reference"><xsl:value-of select="."/></xsl:variable>
		<ipxact:indirectDataRef>
			<xsl:apply-templates select="//ipxact2014:field[@fieldID=$reference]" mode="generateFieldReferenceGroup"/>
		</ipxact:indirectDataRef>
	</xsl:template>

	<!-- generateFieldReferenceGroup -->
	<xsl:template match="ipxact2014:field" mode="generateFieldReferenceGroup">
		<xsl:for-each select="ancestor::*">
			<xsl:if test="not(local-name() = 'component') and ipxact2014:name">
				<xsl:element name="ipxact:{local-name()}Ref" namespace="{$namespace}">
					<xsl:attribute name="{local-name()}Ref"><xsl:value-of select="ipxact2014:name"/></xsl:attribute>
				</xsl:element>
			</xsl:if>
		</xsl:for-each>
		<ipxact:fieldRef>
			<xsl:attribute name="fieldRef"><xsl:value-of select="ipxact2014:name"/></xsl:attribute>
		</ipxact:fieldRef>
	</xsl:template>
	
	<!-- convert white -> clear -->
	<xsl:template match="ipxact2014:whiteboxElementRefs">
		<ipxact:clearboxElementRefs>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:clearboxElementRefs>
	</xsl:template>

	<xsl:template match="ipxact2014:whiteboxElementRef">
		<ipxact:clearboxElementRef>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'clearboxElementRef'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:clearboxElementRef>
	</xsl:template>

	<xsl:template match="ipxact2014:whiteboxElements">
		<ipxact:clearboxElements>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
		</ipxact:clearboxElements>
	</xsl:template>

	<xsl:template match="ipxact2014:whiteboxElement">
		<ipxact:clearboxElement>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'clearboxElement'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:clearboxElement>
	</xsl:template>

	<xsl:template match="ipxact2014:whiteboxType">
		<ipxact:clearboxType>
			<xsl:value-of select="."/>
		</ipxact:clearboxType>
	</xsl:template>

	<!-- Rename @componentRef to @componentInstanceRef -->
	<xsl:template match="ipxact2014:activeInterface/@componentRef | ipxact2014:monitoredActiveInterface/@componentRef | ipxact2014:monitorInterface/@componentRef | ipxact2014:internalPortReference/@componentRef">
		<xsl:attribute name="componentInstanceRef"><xsl:value-of select="."/></xsl:attribute>
	</xsl:template>

	<!-- Convert pathSegment-->
	<xsl:template match="ipxact2014:pathSegment">
		<ipxact:pathSegment>
			<xsl:value-of select="ipxact2014:pathSegmentName"/><xsl:for-each select="ipxact2014:indices/ipxact2014:index">[<xsl:value-of select="."/>]</xsl:for-each>
		</ipxact:pathSegment>
	</xsl:template>

<!--	
	<xsl:template match="ipxact2014:pathSegment/ipxact2014:indices">
		<xsl:call-template name="insertComment">
			<xsl:with-param name="number">1</xsl:with-param>
			<xsl:with-param name="message">Unable to automatically upconvert pathSegment/indices.</xsl:with-param>
		</xsl:call-template>
	</xsl:template> 
-->

	<!-- add CPU memoryMap if no memoryMaps -->	
	<xsl:template match="ipxact2014:addressSpaces">
		<ipxact:addressSpaces>
			<xsl:apply-templates select="ipxact2014:addressSpace"/>
		</ipxact:addressSpaces>
		
		<xsl:if test="not(../ipxact2014:memoryMaps) and ../ipxact2014:cpus/ipxact2014:cpu/ipxact2014:addressSpaceRef">
			<ipxact:memoryMaps>
				<xsl:for-each select="../ipxact2014:cpus/ipxact2014:cpu">
					<ipxact:memoryMap>
						<ipxact:name><xsl:value-of select="ipxact2014:name"/>_MemoryMap</ipxact:name>
						<xsl:for-each select="ipxact2014:addressSpaceRef">
							<xsl:variable name="addressSpaceRef" select="@addressSpaceRef"/>
							<xsl:for-each select="//ipxact2014:busInterfaces/ipxact2014:busInterface/ipxact2014:master[ipxact2014:addressSpaceRef/@addressSpaceRef = $addressSpaceRef]">
								<ipxact:subspaceMap>
									<xsl:attribute name="initiatorRef"><xsl:value-of select="../ipxact2014:name"/></xsl:attribute>
									<ipxact:name><xsl:value-of select="../ipxact2014:name"/>_SubspaceMap</ipxact:name>

									<xsl:if test="not(ipxact2014:addressSpaceRef/ipxact2014:baseAddress)">
										<ipxact:baseAddress>0</ipxact:baseAddress>
									</xsl:if>
									<xsl:if test="ipxact2014:addressSpaceRef/ipxact2014:baseAddress">
										<ipxact:baseAddress><xsl:value-of select="ipxact2014:addressSpaceRef/ipxact2014:baseAddress"/></ipxact:baseAddress>
									</xsl:if>

									<xsl:if test="ipxact2014:isPresent">
										<xsl:call-template name="convertIsPresent">
											<xsl:with-param name="vendor-extension-name" select="'subspaceMap'"/>
										</xsl:call-template>
									</xsl:if>
								</ipxact:subspaceMap>
							</xsl:for-each>
						</xsl:for-each>
					</ipxact:memoryMap>
				</xsl:for-each>
			</ipxact:memoryMaps>
		</xsl:if>
	</xsl:template>

	<!-- add CPU memoryMap if memoryMaps -->	
	<xsl:template match="ipxact2014:memoryMaps">
		<ipxact:memoryMaps>
			<xsl:apply-templates select="ipxact2014:memoryMap"/>
			<xsl:if test="../ipxact2014:cpus/ipxact2014:cpu/ipxact2014:addressSpaceRef">
				<xsl:for-each select="../ipxact2014:cpus/ipxact2014:cpu">
					<ipxact:memoryMap>
						<ipxact:name><xsl:value-of select="ipxact2014:name"/>_MemoryMap</ipxact:name>
						<xsl:for-each select="ipxact2014:addressSpaceRef">
							<xsl:variable name="addressSpaceRef" select="@addressSpaceRef"/>
							<xsl:for-each select="//ipxact2014:busInterfaces/ipxact2014:busInterface/ipxact2014:master[ipxact2014:addressSpaceRef/@addressSpaceRef = $addressSpaceRef]">
								<ipxact:subspaceMap>
									<xsl:attribute name="initiatorRef"><xsl:value-of select="../ipxact2014:name"/></xsl:attribute>
									<ipxact:name><xsl:value-of select="../ipxact2014:name"/>_SubspaceMap</ipxact:name>
									<xsl:if test="not(ipxact2014:addressSpaceRef/ipxact2014:baseAddress)">
										<ipxact:baseAddress>0</ipxact:baseAddress>
									</xsl:if>
									<xsl:if test="ipxact2014:addressSpaceRef/ipxact2014:baseAddress">
										<ipxact:baseAddress><xsl:value-of select="ipxact2014:addressSpaceRef/ipxact2014:baseAddress"/></ipxact:baseAddress>
									</xsl:if>
									
									<xsl:if test="ipxact2014:isPresent">
										<xsl:call-template name="convertIsPresent">
											<xsl:with-param name="vendor-extension-name" select="'subspaceMap'"/>
										</xsl:call-template>
									</xsl:if>
								</ipxact:subspaceMap>
							</xsl:for-each>
						</xsl:for-each>
					</ipxact:memoryMap>
				</xsl:for-each>
			</xsl:if>
		</ipxact:memoryMaps>
	</xsl:template>

	<!-- convert cpu memoryMapRef if addressSpaceRefs -->	
	<xsl:template match="ipxact2014:cpu">
		<ipxact:cpu>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:displayName"/>
			<xsl:apply-templates select="ipxact2014:description"/>
			<xsl:if test="ipxact2014:addressSpaceRef">
				<xsl:variable name="addressSpaceRefName" select="ipxact2014:addressSpaceRef/@addressSpaceRef"/>
				<xsl:comment>Warning: The range has not been calculated please ensure it matches the expected CPU range.</xsl:comment>
				<xsl:text>
		 </xsl:text>
				<ipxact:range>'h10000000000</ipxact:range>
				<ipxact:width><xsl:value-of select="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:width"/></ipxact:width>
				<xsl:if test="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:addressUnitBits">
					<ipxact:addressUnitBits><xsl:value-of select="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:addressUnitBits"/></ipxact:addressUnitBits>
				</xsl:if>
				<xsl:if test="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:executableImage">
					<ipxact:executableImage>
						<xsl:apply-templates select="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:executableImage/@*"/>
						<xsl:apply-templates select="//ipxact2014:addressSpaces/ipxact2014:addressSpace[ipxact2014:name=$addressSpaceRefName]/ipxact2014:executableImage/*"/>
					</ipxact:executableImage>
				</xsl:if>
				<ipxact:memoryMapRef><xsl:value-of select="ipxact2014:name"/>_MemoryMap</ipxact:memoryMapRef>
			</xsl:if>
			<xsl:apply-templates select="ipxact2014:parameters"/>
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:cpu>
	</xsl:template>
	
	<!-- remove executable image from addressSpaces -->
	<xsl:template match="ipxact2014:addressSpace/ipxact2014:executableImage"/>
	
	<!-- convert register -->
	<xsl:template match="ipxact2014:register">
		<ipxact:register>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:displayName"/>
			<xsl:apply-templates select="ipxact2014:description"/>
			<xsl:apply-templates select="ipxact2014:accessHandles"/>
			
			<xsl:if test="ipxact2014:dim">
				<ipxact:array>
					<xsl:for-each select="ipxact2014:dim">
						<ipxact:dim><xsl:value-of select="."/></ipxact:dim>
					</xsl:for-each>
				</ipxact:array>
			</xsl:if>
			
			<xsl:apply-templates select="ipxact2014:addressOffset"/>
			<xsl:apply-templates select="ipxact2014:typeIdentifier"/>
			
			<xsl:apply-templates select="ipxact2014:size"/>
			<xsl:apply-templates select="ipxact2014:volatile"/>
			<xsl:apply-templates select="ipxact2014:access"/>
			<xsl:apply-templates select="ipxact2014:field"/>
			
			<xsl:apply-templates select="ipxact2014:alternateRegisters"/>
			<xsl:apply-templates select="ipxact2014:parameters"/>
			
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:register>
	</xsl:template>
	
	<!-- convert registerFile -->
	<xsl:template match="ipxact2014:registerFile">
		<ipxact:registerFile>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:displayName"/>
			<xsl:apply-templates select="ipxact2014:description"/>
			<xsl:apply-templates select="ipxact2014:accessHandles"/>
			
			<xsl:if test="ipxact2014:dim">
				<ipxact:array>
					<xsl:for-each select="ipxact2014:dim">
						<ipxact:dim><xsl:value-of select="."/></ipxact:dim>
					</xsl:for-each>
				</ipxact:array>
			</xsl:if>
			
			<xsl:apply-templates select="ipxact2014:addressOffset"/>
			<xsl:apply-templates select="ipxact2014:typeIdentifier"/>
			
			<xsl:apply-templates select="ipxact2014:range"/>

			<xsl:apply-templates select="ipxact2014:register | ipxact2014:registerFile"/>
			
			<xsl:apply-templates select="ipxact2014:parameters"/>
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:registerFile>
	</xsl:template>
	
	<xsl:template match="ipxact2014:mirroredSlave/ipxact2014:baseAddresses">
		<ipxact:baseAddresses>
			<xsl:for-each select="ipxact2014:remapAddress">
				<ipxact:remapAddresses>
					<ipxact:remapAddress><xsl:value-of select="."/></ipxact:remapAddress>
					<xsl:if test="@state">
						<ipxact:modeRef priority="0"><xsl:value-of select="@state"/></ipxact:modeRef>
					</xsl:if>
				</ipxact:remapAddresses>
			</xsl:for-each>
			<ipxact:range><xsl:value-of select="ipxact2014:range"/></ipxact:range>
		</ipxact:baseAddresses>
	</xsl:template>

	<!-- remapStates, resetTypes, alternateGroups >> modes -->
	<xsl:template match="ipxact2014:remapStates">
		<ipxact:modes>
			<xsl:for-each select="ipxact2014:remapState">
				<ipxact:mode>
					<xsl:apply-templates select="ipxact2014:name"/>
					<xsl:apply-templates select="ipxact2014:displayName"/>
					<xsl:apply-templates select="ipxact2014:description"/>
					<xsl:if test="ipxact2014:remapPorts/ipxact2014:remapPort">
						<ipxact:condition>
							<xsl:for-each select="ipxact2014:remapPorts/ipxact2014:remapPort">
								<xsl:value-of select="@portRef"/><xsl:if test="ipxact2014:portIndex">[<xsl:value-of select="ipxact2014:portIndex"/>]</xsl:if> = <xsl:value-of select="ipxact2014:value"/><xsl:if test="not(position() = last())"> &amp;&amp; </xsl:if>
							</xsl:for-each>
						</ipxact:condition>
					</xsl:if>
				</ipxact:mode>
			</xsl:for-each>
			<xsl:for-each select="../ipxact2014:resetTypes/ipxact2014:resetType">
				<ipxact:mode>
					<ipxact:name>resetType_<xsl:value-of select="ipxact2014:name"/></ipxact:name>
					<xsl:apply-templates select="ipxact2014:displayName"/>
					<xsl:apply-templates select="ipxact2014:description"/>
					<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
					<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
						<xsl:call-template name="convertIsPresent"/>
					</xsl:if>
				</ipxact:mode>
			</xsl:for-each>
			<xsl:for-each select="..//ipxact2014:register/ipxact2014:alternateRegisters/ipxact2014:alternateRegister/ipxact2014:alternateGroups/ipxact2014:alternateGroup[not(.=preceding::*)]">
				<ipxact:mode>
					<ipxact:name>alternateGroup_<xsl:value-of select="."/></ipxact:name>
				</ipxact:mode>
			</xsl:for-each>
		</ipxact:modes>
	</xsl:template>

	<!-- memoryRemap -->
	<xsl:template match="ipxact2014:memoryRemap">
		<ipxact:memoryRemap>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:displayName"/>
			<xsl:apply-templates select="ipxact2014:description"/>
			<ipxact:modeRef priority="0"><xsl:value-of select="@state"/></ipxact:modeRef>
			<xsl:apply-templates select="ipxact2014:addressBlock | ipxact2014:bank | ipxact2014:subspaceMap"/>
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:memoryRemap>
	</xsl:template>

	<!-- convert field -->
	<xsl:template match="ipxact2014:field">
		<ipxact:field>
			<xsl:apply-templates select="ipxact2014:name"/>
			<xsl:apply-templates select="ipxact2014:displayName"/>
			<xsl:apply-templates select="ipxact2014:description"/>
			<xsl:apply-templates select="ipxact2014:accessHandles"/>
			<xsl:apply-templates select="ipxact2014:bitOffset"/>
			<xsl:apply-templates select="ipxact2014:typeIdentifier"/>
			<xsl:apply-templates select="ipxact2014:array"/>
			<xsl:apply-templates select="ipxact2014:bitWidth"/>
			<xsl:apply-templates select="ipxact2014:volatile"/>
			<xsl:apply-templates select="ipxact2014:resets"/>
			
			<xsl:if test="ipxact2014:access | ipxact2014:modifiedWriteValue | ipxact2014:writeValueConstraint | ipxact2014:readAction | ipxact2014:testable | ipxact2014:reserved">
				<ipxact:fieldAccessPolicies>
					<ipxact:fieldAccessPolicy>
						<xsl:apply-templates select="ipxact2014:access"/>
						<xsl:apply-templates select="ipxact2014:modifiedWriteValue"/>
						<xsl:apply-templates select="ipxact2014:writeValueConstraint"/>
						<xsl:apply-templates select="ipxact2014:readAction"/>
						<xsl:apply-templates select="ipxact2014:testable"/>
						<xsl:apply-templates select="ipxact2014:reserved"/>
					</ipxact:fieldAccessPolicy>
				</ipxact:fieldAccessPolicies>
			</xsl:if>
	
			<xsl:apply-templates select="ipxact2014:enumeratedValues"/>
			<xsl:apply-templates select="ipxact2014:parameters"/>
			
			<xsl:apply-templates select="ipxact2014:vendorExtensions"/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent"/>
			</xsl:if>
		</ipxact:field>
	</xsl:template>

	<xsl:template match="ipxact2014:wire/ipxact2014:vectors">
		<ipxact:vectors>
			<xsl:for-each select="ipxact2014:vector">
				<ipxact:vector>
					<xsl:if test="../../ipxact2014:wireTypeDefs/ipxact2014:wireTypeDef/ipxact2014:typeName/@constrained[.='true']">
						<xsl:choose>
							<xsl:when test="count(../ipxact2014:vector) > 1">
								<xsl:attribute name="vectorId">default<xsl:value-of select="position()"/></xsl:attribute>
							</xsl:when>
							<xsl:otherwise>
								<xsl:attribute name="vectorId">default</xsl:attribute>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:if>
					<xsl:apply-templates/>
				</ipxact:vector>
			</xsl:for-each>
		</ipxact:vectors>
	</xsl:template>

	<xsl:template match="ipxact2014:wireTypeDef/ipxact2014:typeName">
		<ipxact:typeName>
			<xsl:if test="@constrained='true' and ../../../ipxact2014:vectors/ipxact2014:vector">
				<xsl:choose>
					<xsl:when test="count(../../../ipxact2014:vectors/ipxact2014:vector) > 1">
						<xsl:attribute name="constrained"><xsl:for-each select="../../../ipxact2014:vectors/ipxact2014:vector">default<xsl:value-of select="position()"/><xsl:text> </xsl:text></xsl:for-each></xsl:attribute>
					</xsl:when>
					<xsl:otherwise>
						<xsl:attribute name="constrained">default</xsl:attribute>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
			<xsl:value-of select="."/>
		</ipxact:typeName>
	</xsl:template>

	<xsl:template match="ipxact2014:reset[@resetType]">
		<ipxact:reset>
			<xsl:apply-templates select="@id"/>
			<ipxact:modeRef priority="0">resetType_<xsl:value-of select="@resetType"/></ipxact:modeRef>
			<xsl:apply-templates select="ipxact2014:value"/>
			<xsl:apply-templates select="ipxact2014:mask"/>
		</ipxact:reset>
	</xsl:template>

	<xsl:template match="ipxact2014:alternateGroups">
		<xsl:for-each select="ipxact2014:alternateGroup">
			<ipxact:modeRef priority="{position()}">alternateGroup_<xsl:value-of select="."/></ipxact:modeRef>
		</xsl:for-each>
	</xsl:template>

	<xsl:template match="ipxact2014:register/ipxact2014:access">
		<ipxact:accessPolicies>
			<ipxact:accessPolicy>
				<ipxact:access><xsl:value-of select="."/></ipxact:access>
			</ipxact:accessPolicy>
		</ipxact:accessPolicies>
	</xsl:template>

	<xsl:template match="ipxact2014:alternateRegister/ipxact2014:access">
		<ipxact:accessPolicies>
			<ipxact:accessPolicy>
				<ipxact:access><xsl:value-of select="."/></ipxact:access>
			</ipxact:accessPolicy>
		</ipxact:accessPolicies>
	</xsl:template>

	<xsl:template match="ipxact2014:addressBlock/ipxact2014:access">
		<ipxact:accessPolicies>
			<ipxact:accessPolicy>
				<ipxact:access><xsl:value-of select="."/></ipxact:access>
			</ipxact:accessPolicy>
		</ipxact:accessPolicies>
	</xsl:template>

	<xsl:template match="ipxact2014:bank/ipxact2014:access">
		<ipxact:accessPolicies>
			<ipxact:accessPolicy>
				<ipxact:access><xsl:value-of select="."/></ipxact:access>
			</ipxact:accessPolicy>
		</ipxact:accessPolicies>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractionDefinition//ipxact2014:port">
		<ipxact:port>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractionDefinitionPort'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:port>
	</xsl:template>
	
	<xsl:template match="/ipxact2014:abstractor//ipxact2014:constraintSetRef">
		<ipxact:constraintSetRef>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorConstraintSetRef'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:constraintSetRef>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:file">
		<ipxact:file>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorFile'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:file>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:fileSetRef">
		<ipxact:fileSetRef>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorFileSetRef'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:fileSetRef>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:port">
		<ipxact:port>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorPort'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:port>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:portMap">
		<ipxact:portMap>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorPortMap'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:portMap>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:moduleParameter">
		<ipxact:moduleParameter>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorModuleParameter'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:moduleParameter>
	</xsl:template>

	<xsl:template match="/ipxact2014:abstractor//ipxact2014:typeParameter">
		<ipxact:typeParameter>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorTypeParameter'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:typeParameter>
	</xsl:template>
	
	<xsl:template match="/ipxact2014:abstractor//ipxact2014:view">
		<ipxact:view>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorView'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:view>
	</xsl:template>
	
	<xsl:template match="/ipxact2014:abstractor//ipxact2014:whiteboxElementRef">
		<ipxact:clearboxElementRef>
			<xsl:apply-templates select="@*"/>
			<xsl:apply-templates/>
			<xsl:if test="not(ipxact2014:vendorExtensions) and ipxact2014:isPresent">
				<xsl:call-template name="convertIsPresent">
					<xsl:with-param name="vendor-extension-name" select="'abstractorClearboxElementRef'"/>
				</xsl:call-template>
			</xsl:if>
		</ipxact:clearboxElementRef>
	</xsl:template>

	<!-- remove isPresent elements -->
	<xsl:template match="ipxact2014:isPresent"/>
		
	<!-- add isPresent to existing vendorExtensions element -->
	<xsl:template match="ipxact2014:vendorExtensions">
		<ipxact:vendorExtensions>
			<xsl:if test="../ipxact2014:isPresent">
				<xsl:choose>
					<xsl:when test="/*[local-name() = 'abstractionDefinition'] and local-name(..) = 'port'">
						<xsl:element name="accellera:abstractionDefinitionPort" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'constraintSetRef'">
						<xsl:element name="accellera:abstractorConstraintSetRef" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'file'">
						<xsl:element name="accellera:abstractorFile" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'fileSetRef'">
						<xsl:element name="accellera:abstractorFileSetRef" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'port'">
						<xsl:element name="accellera:abstractorPort" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'portMap'">
						<xsl:element name="accellera:abstractorPortMap" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'moduleParameter'">
						<xsl:element name="accellera:abstractorModuleParameter" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'typeParameter'">
						<xsl:element name="accellera:abstractorTypeParameter" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'view'">
						<xsl:element name="accellera:abstractorView" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="/*[local-name() = 'abstractor'] and local-name(..) = 'whiteboxElementRef'">
						<xsl:element name="accellera:abstractorClearboxElementRef" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="local-name(..) = 'whiteboxElementRef'">
						<xsl:element name="accellera:clearboxElementRef" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:when test="local-name(..) = 'whiteboxElement'">
						<xsl:element name="accellera:clearboxElement" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:otherwise>
						<xsl:element name="accellera:{local-name(..)}" namespace="{$VE.namespace}">
							<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="../ipxact2014:isPresent"/></xsl:element>
						</xsl:element>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
			<xsl:apply-templates select="*"/>
		</ipxact:vendorExtensions>
	</xsl:template>

	<!-- add isPresent when no vendorExtensions element -->
	<xsl:template name="convertIsPresent">
		<xsl:param name="vendor-extension-name" select="local-name()"/>
		<xsl:if test="ipxact2014:isPresent">
			<ipxact:vendorExtensions>
				<xsl:element name="accellera:{$vendor-extension-name}" namespace="{$VE.namespace}">
					<xsl:element name="accellera-cond:isPresent" namespace="{$COND.namespace}"><xsl:value-of select="ipxact2014:isPresent"/></xsl:element>
				</xsl:element>
			</ipxact:vendorExtensions>
		</xsl:if>
	</xsl:template>
</xsl:stylesheet>
