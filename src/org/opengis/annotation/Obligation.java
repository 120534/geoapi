/*$************************************************************************************************
 **
 ** $Id$
 **
 ** $Source$
 **
 ** Copyright (C) 2003 Open GIS Consortium, Inc. All Rights Reserved. http://www.opengis.org/Legal/
 **
 *************************************************************************************************/
package org.opengis.annotation;


/**
 * Obligation of the element or entity. The enum values declared here are an exact copy of
 * the code list elements declared in the {@link org.opengis.metadata.Obligation} code list
 * from the metadata package.
 * 
 * @author ISO 19115
 * @author <A HREF="http://www.opengis.org">OpenGIS&reg; consortium</A>
 * @version <A HREF="http://www.opengis.org/docs/01-111.pdf">Abstract specification 5.0</A>
 */
@UML(identifier="MD_ObligationCode")
public enum Obligation {
    /**
     * Element is required when a specific condition is met.
     */
    @UML(identifier="conditional", obligation=CONDITIONAL)
    CONDITIONAL,

    /**
     * Element is not required.
     */
    @UML(identifier="optional", obligation=CONDITIONAL)
    OPTIONAL,

    /**
     * Element is always required.
     */
    @UML(identifier="mandatory", obligation=CONDITIONAL)
    MANDATORY
}