/*
 * Copyright (C) 2003 Open GIS Consortium, Inc. All Rights Reserved. http://www.opengis.org/Legal/
 */
package org.opengis.cs;


/**
 * A three-dimensional coordinate system with one distance measured from the origin and two
 * angular coordinates. Not to be confused with an {@linkplain EllipsoidalCS ellipsoidal
 * coordinate system} based on an ellipsoid "degenerated" into a sphere.
 * A <code>SphericalCS</code> shall have three {@linkplain #getAxis axis associations}.
 *
 * <TABLE CELLPADDING='6' BORDER='1'>
 * <TR BGCOLOR="#EEEEFF"><TH NOWRAP>Used with CRS type(s)</TH></TR>
 * <TR><TD>
 *   {@link org.opengis.sc.GeocentricCRS  Geocentric},
 *   {@link org.opengis.sc.EngineeringCRS Engineering}
 * </TD></TR></TABLE>
 *
 * @UML abstract CS_SphericalCS
 * @author ISO 19111
 * @author <A HREF="http://www.opengis.org">OpenGIS&reg; consortium</A>
 * @version 2.0
 */
public interface SphericalCS extends CoordinateSystem {
}
