<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>
        <xsl:template match="/service">
        <html>
            <head>
                <style>
                    table { width: 100%; border-collapse: collapse; }
                    th { color: white; background-color: #4CAF50; }
                    th, td { padding: 8px; text-align: left; border: 1px solid black; }
                    h1 { text-align: center; }
                </style>
            </head>
            <body>
                <h1><xsl:value-of select="@id"/> Interface</h1>
                <table>
                    <tr>
                        <th>Method(s)</th>
                        <th>Parameter(s)</th>
                        <th>Return</th>
                        <th>Number of Exception(s)</th>
                    </tr>
                    <xsl:for-each select="abstract_method">
                        <tr>
                            <td><xsl:value-of select="@name"/></td>
                            <td>
                                <xsl:for-each select="arguments/parameter">
                                    <xsl:value-of select="text()"/>: <xsl:value-of select="@type"/>
                                    <xsl:if test="position() != last()">, <br/></xsl:if>
                                </xsl:for-each>
                            </td>
                            <td><xsl:value-of select="return"/></td>
                            <td><xsl:value-of select="count(exceptions/exception)"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
