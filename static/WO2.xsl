<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:skos="http://www.w3.org/2004/02/skos/core#"
    exclude-result-prefixes="rdf skos"
    version="3.0">
    
  <xsl:output method="xml" indent="yes"/>  <!-- no in production! --> 
  
  <xsl:template match="/" >
  <adlibXML>
    <recordList>
    <xsl:apply-templates select="//rdf:Description" />
    </recordList>
  </adlibXML>
  </xsl:template>
  
  <xsl:template match="//rdf:Description">
    <record>
      <WO2_URL><xsl:value-of select="skos:Concept/@rdf:resource" /></WO2_URL>
      <source.number><xsl:value-of select="skos:Concept/@rdf:resource" /></source.number>
      <term.number><xsl:value-of select="skos:Concept/@rdf:resource" /></term.number>
      <term><xsl:value-of select="skos:prefLabel" /></term>
      <scope_note><xsl:value-of select="skos:scopeNote" /></scope_note>
      <WO2_scope_note><xsl:value-of select="skos:scopeNote" /></WO2_scope_note>
      <xsl:for-each select="skos:altLabel">
        <used_for><xsl:value-of select="." /></used_for>
      </xsl:for-each>
      <xsl:for-each select="skos:broaderLabel[not(.=preceding::*)]">
        <broader.term><xsl:value-of select="." /></broader.term>
      </xsl:for-each>
    </record>
  </xsl:template>

</xsl:stylesheet>  