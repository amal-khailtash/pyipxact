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
<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	xmlns:spirit15="http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5">

<xsl:param name="namespace" select="'http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009'"/>

<xsl:strip-space elements="*"/>
<xsl:output method="xml" indent="yes"/>

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
  </xsl:copy><xsl:text>
</xsl:text>
</xsl:template>

<xsl:template match="@*">
  <xsl:attribute name="{name()}" namespace="{namespace-uri()}">
    <xsl:value-of select="."/>
  </xsl:attribute>
</xsl:template>

<xsl:template match="/spirit15:*">
  <xsl:element name="spirit:{local-name()}" namespace="{$namespace}">
    <xsl:for-each select="namespace::*">
      <xsl:if test="not(.='http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5')">
        <xsl:copy/>
      </xsl:if>
    </xsl:for-each>
    <xsl:apply-templates select="@*"/>
    <xsl:apply-templates/>
  </xsl:element>
</xsl:template>

<xsl:template match="@xsi:schemaLocation">
  <xsl:attribute name="xsi:schemaLocation">
    <xsl:text>http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009 http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009/index.xsd</xsl:text>
  </xsl:attribute>
</xsl:template>

<xsl:template match="spirit15:*">
  <xsl:element name="spirit:{local-name()}" namespace="{$namespace}">
    <xsl:apply-templates select="@*"/>
    <xsl:apply-templates/>
  </xsl:element>
</xsl:template>

<!-- The attributes need to be handled a little differently, to avoid confusing the 
    processor, the namespaceURI should not be explicitly defined -->
<xsl:template match="@spirit15:*">
  <xsl:attribute name="spirit:{local-name()}" namespace="{$namespace}">
    <xsl:value-of select="."/>
  </xsl:attribute>
</xsl:template>

</xsl:stylesheet>
