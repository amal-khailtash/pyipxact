<?xml version="1.0"?>
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
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:xalan="http://xml.apache.org/xalan" xmlns:exslt="http://exslt.org/common" exclude-result-prefixes="exslt xalan msxsl" xmlns:msxsl="urn:schemas-microsoft-com:xslt">
	<xsl:include href="convert_expressions.xsl"/>
	<xsl:output method="xml" indent="yes" encoding="UTF-8"/>

	<!-- xalan -->
	<xsl:template name="xalan:parse">
		<xsl:param name="value" select="''"/>
		<xsl:variable name="tokens">
			<xsl:call-template name="tokenize">
				<xsl:with-param name="value" select="$value"/>
				<xsl:with-param name="delimiters" select="concat($apos, $quot, '(&#x20;),=*+&lt;>-')"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:variable name="valid">
			<xsl:call-template name="xalan:validate">
				<xsl:with-param name="tokens" select="$tokens"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="not(contains($valid, 'false'))">
				<xsl:call-template name="xalan:replace">
					<xsl:with-param name="tokens" select="$tokens"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$value"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	<xsl:template name="xalan:validate">
		<xsl:param name="tokens"/>
		<xsl:if test="$debug">
			<xsl:message>validate("<xsl:value-of select="$tokens"/>") [<xsl:value-of select="count(xalan:nodeset($tokens)/token)"/>]</xsl:message>
			<xsl:message>
				<token>
					<xsl:attribute name="type"><xsl:value-of select="xalan:nodeset($tokens)/token[1]/@type"/></xsl:attribute>
					<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
				</token>
			</xsl:message>
		</xsl:if>
		<xsl:if test="count(xalan:nodeset($tokens)/token) > 0">
			<xsl:variable name="token" select="xalan:nodeset($tokens)/token[1]"/>
			<xsl:choose>
				<xsl:when test="$token/@type = 'string'">
					<!-- Continue -->
					<xsl:call-template name="xalan:validate">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="contains($token, '/') or contains($token, '::') or contains($token, '[') or contains($token, ']') or contains($token, '..') or contains($token, '@')">
					<xsl:message>ERROR: XPath Location Paths cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath Location Paths cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="starts-with($token, '$')">
					<xsl:message>ERROR: XPath Variable References cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath Variable References cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'last'">
					<xsl:message>ERROR: XPath last() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath last() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'position'">
					<xsl:message>ERROR: XPath position() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath position() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'count'">
					<xsl:message>ERROR: XPath count() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath count() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'local-name'">
					<xsl:message>ERROR: XPath local-name() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath local-name() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'namespace-uri'">
					<xsl:message>ERROR: XPath namespace-uri() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath namespace-uri() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'name'">
					<xsl:message>ERROR: XPath name() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath name() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'string'">
					<xsl:message>ERROR: XPath string() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath string() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'starts-with'">
					<xsl:message>ERROR: XPath starts-with() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath starts-with() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'contains'">
					<xsl:message>ERROR: XPath contains() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath contains() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'substring-before'">
					<xsl:message>ERROR: XPath substring-before() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath substring-before() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'substring-after'">
					<xsl:message>ERROR: XPath substring-after() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath substring-after() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'substring'">
					<xsl:message>ERROR: XPath substring() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath substring() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'string-length'">
					<xsl:message>ERROR: XPath string-length() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath string-length() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'normalize-space'">
					<xsl:message>ERROR: XPath normalize-space() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath normalize-space() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'translate'">
					<xsl:message>ERROR: XPath translate() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath translate() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'lang'">
					<xsl:message>ERROR: XPath lang() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath lang() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'number' and xalan:nodeset($tokens)/token[2] = '(' and xalan:nodeset($tokens)/token[3] = ')'">
					<xsl:message>ERROR: XPath number() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath number() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="$token = 'sum'">
					<xsl:message>ERROR: XPath sum() function cannot be converted.</xsl:message>
					<xsl:comment>ERROR: XPath sum() function cannot be converted.</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:when test="contains($token, ':containsToken')">
					<xsl:message>WARNING: XPath containsToken() function cannot be automatically converted, please convert manually!</xsl:message>
					<xsl:comment>WARNING: XPath containsToken() function cannot be automatically converted, please convert manually!</xsl:comment>
					<xsl:text>false</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<!-- Continue -->
					<xsl:call-template name="xalan:validate">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>
	
	<xsl:template name="xalan:replace">
		<xsl:param name="tokens"/>
		<xsl:if test="$debug">
			<xsl:message>replace("<xsl:value-of select="xalan:nodeset($tokens)"/>") [<xsl:value-of select="count(xalan:nodeset($tokens)/token)"/>]</xsl:message>
			<xsl:message>
				<token>
					<xsl:attribute name="type"><xsl:value-of select="xalan:nodeset($tokens)/token[1]/@type"/></xsl:attribute>
					<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
				</token>
			</xsl:message>
		</xsl:if>
		<xsl:if test="count(xalan:nodeset($tokens)/token) > 0">
			<xsl:choose>
				<xsl:when test="xalan:nodeset($tokens)/token[1]/@type = 'string'">
					<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'true'">
					<xsl:text>1</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 3]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'false'">
					<xsl:text>0</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 3]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'and'">
					<xsl:text> &amp;&amp; </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'div'">
					<xsl:text> / </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'mod'">
					<xsl:text> % </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'id'">
					<xsl:value-of select="xalan:nodeset($tokens)/token[4]"/>
					<xsl:call-template name="add-space">
						<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[7]"/>
					</xsl:call-template>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 6]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'boolean'">
					<xsl:text>bit'</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'not'">
					<xsl:text>!</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'number'">
				  <xsl:text>real'</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'floor'">
					<xsl:text>$floor</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'ceiling'">
					<xsl:text>$ceil</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'round'">
					<xsl:text>longint'</xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '='">
					<xsl:text> == </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '&lt;'">
				  <xsl:choose>
				    <xsl:when test="xalan:nodeset($tokens)/token[2] = '='">
    					<xsl:text> &lt;= </xsl:text>
    					<xsl:call-template name="xalan:replace">
    						<xsl:with-param name="tokens">
    							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
    								<xsl:copy-of select="."/>
    							</xsl:for-each>
    						</xsl:with-param>
    					</xsl:call-template>
				    </xsl:when>
				    <xsl:otherwise>
    					<xsl:text> &lt; </xsl:text>
    					<xsl:call-template name="xalan:replace">
    						<xsl:with-param name="tokens">
    							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
    								<xsl:copy-of select="."/>
    							</xsl:for-each>
    						</xsl:with-param>
    					</xsl:call-template>
				    </xsl:otherwise>
				  </xsl:choose>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '>'">
				  <xsl:choose>
				    <xsl:when test="xalan:nodeset($tokens)/token[2] = '='">
    					<xsl:text> >= </xsl:text>
    					<xsl:call-template name="xalan:replace">
    						<xsl:with-param name="tokens">
    							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
    								<xsl:copy-of select="."/>
    							</xsl:for-each>
    						</xsl:with-param>
    					</xsl:call-template>
				    </xsl:when>
				    <xsl:otherwise>
    					<xsl:text> > </xsl:text>
    					<xsl:call-template name="xalan:replace">
    						<xsl:with-param name="tokens">
    							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
    								<xsl:copy-of select="."/>
    							</xsl:for-each>
    						</xsl:with-param>
    					</xsl:call-template>
				    </xsl:otherwise>
				  </xsl:choose>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '*'">
					<xsl:text> * </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '-'">
					<xsl:text> - </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = '+'">
					<xsl:text> + </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="contains(xalan:nodeset($tokens)/token[1], ':pow')">
					<xsl:variable name="closing-bracket-location">
						<xsl:call-template name="xalan:find-closing-bracket">
							<xsl:with-param name="tokens">
								<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
									<xsl:copy-of select="."/>
								</xsl:for-each>
							</xsl:with-param>
						</xsl:call-template>
					</xsl:variable>

					<xsl:text>longint'($pow</xsl:text>
					
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1 and position() &lt;= $closing-bracket-location]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
					<xsl:text>)</xsl:text>

					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > $closing-bracket-location]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
					
				</xsl:when>
				<xsl:when test="contains(xalan:nodeset($tokens)/token[1], ':log')">
					<xsl:variable name="comma-location">
						<xsl:call-template name="xalan:find-token">
							<xsl:with-param name="tokens">
								<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
									<xsl:copy-of select="."/>
								</xsl:for-each>
							</xsl:with-param>
							<xsl:with-param name="token" select="','"/>
						</xsl:call-template>
					</xsl:variable>
					<xsl:variable name="end-bracket-location">
						<xsl:call-template name="xalan:find-token">
							<xsl:with-param name="tokens">
								<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
									<xsl:copy-of select="."/>
								</xsl:for-each>
							</xsl:with-param>
							<xsl:with-param name="token" select="')'"/>
						</xsl:call-template>
					</xsl:variable>
					<xsl:choose>
						<xsl:when test="$comma-location = 2 and xalan:nodeset($tokens)/token[3] = '10'">
							<xsl:text>$log10(</xsl:text>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > ($comma-location + 2) and position() &lt; ($end-bracket-location + 2)]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:text>)</xsl:text>
							<xsl:call-template name="add-space">
								<xsl:with-param name="next-token" select="$end-bracket-location + 3"/>
							</xsl:call-template>
						</xsl:when>
						<xsl:otherwise>
							<xsl:text>$ln(</xsl:text>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > ($comma-location + 2) and position() &lt; ($end-bracket-location + 2)]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:text>)/$ln(</xsl:text>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2 and position() &lt; ($comma-location + 2)]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:text>)</xsl:text>
							<xsl:call-template name="add-space">
								<xsl:with-param name="next-token" select="$end-bracket-location + 3"/>
							</xsl:call-template>
						</xsl:otherwise>
					</xsl:choose>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > $end-bracket-location + 2]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'or'">
					<xsl:text> || </xsl:text>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="contains(xalan:nodeset($tokens)/token[1], ':decode')">
					<xsl:choose>
						<xsl:when test="xalan:nodeset($tokens)/token[3] = $apos or xalan:nodeset($tokens)/token[3] = $quot">
							<xsl:call-template name="parse-scale">
								<xsl:with-param name="value" select="xalan:nodeset($tokens)/token[4]"/>
							</xsl:call-template>
							<xsl:call-template name="add-space">
								<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[7]"/>
							</xsl:call-template>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 6]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:when>
						<xsl:when test="xalan:nodeset($tokens)/token[3] = 'id'">
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2 and position() &lt; 9]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
							<xsl:call-template name="add-space">
								<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[7]"/>
							</xsl:call-template>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 9]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:when>
					</xsl:choose>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[1] = 'concat'">
					<xsl:text>{</xsl:text>
					<xsl:variable name="location">
						<xsl:call-template name="xalan:find-token">
							<xsl:with-param name="tokens">
								<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
									<xsl:copy-of select="."/>
								</xsl:for-each>
							</xsl:with-param>
							<xsl:with-param name="token" select="')'"/>
						</xsl:call-template>
					</xsl:variable>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2 and position() &lt; ($location + 2)]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
					<xsl:text>}</xsl:text>
					<xsl:call-template name="add-space">
						<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[$location + 3]"/>
					</xsl:call-template>
					<xsl:call-template name="xalan:replace">
						<xsl:with-param name="tokens">
							<xsl:for-each select="xalan:nodeset($tokens)/token[position() > ($location + 2)]">
								<xsl:copy-of select="."/>
							</xsl:for-each>
						</xsl:with-param>
					</xsl:call-template>
				</xsl:when>
				<xsl:otherwise>
					<xsl:choose>
						<xsl:when test="xalan:nodeset($tokens)/token[2] = '='">
							<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
							<xsl:choose>
								<xsl:when test="contains(xalan:nodeset($tokens)/token[1], '!') or contains(xalan:nodeset($tokens)/token[1], '>') or contains(xalan:nodeset($tokens)/token[1], '&lt;')">
									<xsl:text>=</xsl:text>
									<xsl:call-template name="add-space">
										<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[3]"/>
									</xsl:call-template>
									<xsl:call-template name="xalan:replace">
										<xsl:with-param name="tokens">
											<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 2]">
												<xsl:copy-of select="."/>
											</xsl:for-each>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:when>
								<xsl:otherwise>
									<xsl:text> </xsl:text>
									<xsl:call-template name="xalan:replace">
										<xsl:with-param name="tokens">
											<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
												<xsl:copy-of select="."/>
											</xsl:for-each>
										</xsl:with-param>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:when>
						<xsl:otherwise>
							<xsl:choose>
								<xsl:when test="xalan:nodeset($tokens)/token[1] = ')'">
									<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
									<xsl:call-template name="add-space">
										<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[2]"/>
									</xsl:call-template>
								</xsl:when>
								<xsl:when test="xalan:nodeset($tokens)/token[1] = '(' or xalan:nodeset($tokens)/token[2] = ')' or xalan:nodeset($tokens)/token[2] = ',' or xalan:nodeset($tokens)/token[1] = $apos or xalan:nodeset($tokens)/token[1] = $quot">
									<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
								</xsl:when>
								<xsl:otherwise>
									<xsl:value-of select="xalan:nodeset($tokens)/token[1]"/>
									<xsl:call-template name="add-space">
										<xsl:with-param name="next-token" select="xalan:nodeset($tokens)/token[2]"/>
									</xsl:call-template>
								</xsl:otherwise>
							</xsl:choose>
							<xsl:call-template name="xalan:replace">
								<xsl:with-param name="tokens">
									<xsl:for-each select="xalan:nodeset($tokens)/token[position() > 1]">
										<xsl:copy-of select="."/>
									</xsl:for-each>
								</xsl:with-param>
							</xsl:call-template>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>
	
	<!-- Finds a token, making sure the token is located at the same level (identified by '(' and ')' brackets) as where the search started, i.e. outside any internal brackets. -->
	<xsl:template name="xalan:find-token">
		<xsl:param name="tokens"/>
		<xsl:param name="token"/>
		<xsl:param name="index" select="1"/>
		<xsl:param name="level" select="0"/>
		<xsl:if test="debug">
			<xsl:message>find-token(<xsl:value-of select="xalan:nodeset($tokens)"/>, <xsl:value-of select="$token"/>, <xsl:value-of select="$index"/>) [<xsl:value-of select="xalan:nodeset($tokens)/token[$index]"/>]</xsl:message>
		</xsl:if>
		<xsl:if test="$level >= 0 and count(xalan:nodeset($tokens)/token) > 0">
			<xsl:choose>
				<xsl:when test="$level = 0 and xalan:nodeset($tokens)/token[$index] = $token">
					<xsl:value-of select="$index"/>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[$index] = '('">
					<xsl:call-template name="xalan:find-token">
						<xsl:with-param name="tokens" select="$tokens"/>
						<xsl:with-param name="token" select="$token"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level + 1"/>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[$index] = ')'">
					<xsl:call-template name="xalan:find-token">
						<xsl:with-param name="tokens" select="$tokens"/>
						<xsl:with-param name="token" select="$token"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level - 1"/>
					</xsl:call-template>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name="xalan:find-token">
						<xsl:with-param name="tokens" select="$tokens"/>
						<xsl:with-param name="token" select="$token"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level"/>
					</xsl:call-template>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<!-- Finds a token, making sure the token is located at the same level (identified by '(' and ')' brackets) as where the search started, i.e. outside any internal brackets. -->
	<xsl:template name="xalan:find-closing-bracket">
		<xsl:param name="tokens"/>
		<xsl:param name="index" select="1"/>
		<xsl:param name="level" select="1"/>
		
		<xsl:if test="debug">
			<xsl:message>find-closing-bracket(<xsl:value-of select="xalan:nodeset($tokens)"/>, <xsl:value-of select="$index"/>, <xsl:value-of select="$level"/>)</xsl:message>
		</xsl:if>
		
		<xsl:if test="$level = 0 or count(xalan:nodeset($tokens)/token) &lt; $index">
			<xsl:value-of select="$index"/>
		</xsl:if>
		
		<xsl:if test="$level > 0 and count(xalan:nodeset($tokens)/token) >= $index">
			<xsl:choose>
				<xsl:when test="xalan:nodeset($tokens)/token[$index] = '('">
					<xsl:call-template name="xalan:find-closing-bracket">
						<xsl:with-param name="tokens" select="xalan:nodeset($tokens)"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level + 1"/>
					</xsl:call-template>
				</xsl:when>
				<xsl:when test="xalan:nodeset($tokens)/token[$index] = ')'">
					<xsl:call-template name="xalan:find-closing-bracket">
						<xsl:with-param name="tokens" select="xalan:nodeset($tokens)"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level - 1"/>
					</xsl:call-template>
				</xsl:when>
				<xsl:otherwise>
					<xsl:call-template name="xalan:find-closing-bracket">
						<xsl:with-param name="tokens" select="xalan:nodeset($tokens)"/>
						<xsl:with-param name="index" select="$index + 1"/>
						<xsl:with-param name="level" select="$level"/>
					</xsl:call-template>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>
</xsl:stylesheet>
