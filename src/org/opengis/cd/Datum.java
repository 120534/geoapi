/*
 * Copyright (C) 2003 Open GIS Consortium, Inc. All Rights Reserved. http://www.opengis.org/Legal/
 */
package org.opengis.cd;

// J2SE direct dependencies
import java.util.Date;
import java.util.Locale;

// OpenGIS direct dependencies
import org.opengis.ex.Extent;
import org.opengis.rs.Identifier;


/**
 * Specifies the relationship of a coordinate system to the earth, thus creating a coordinate
 * reference system. A datum uses a parameter or set of parameters that determine the location
 * of the origin of the coordinate reference system. Each datum subtype can be associated with
 * only specific types of coordinate systems.
 *
 * @UML abstract CD_Datum
 * @author ISO 19111
 * @author <A HREF="http://www.opengis.org">OpenGIS&reg; consortium</A>
 * @version 2.0
 *
 * @see org.opengis.cs.CoordinateSystem
 * @see org.opengis.sc.CoordinateReferenceSystem
 */
public interface Datum {
    /**
     * The name by which this datum is identified.
     *
     * @return The datum name.
     * @UML mandatory datumName
     *
     * @rename  Omitted the "<code>datum</code>" prefix.
     */
    public String getName();

    /**
     * Set of alternative identifications of this datum. The first identifier, if any,
     * is normally the primary identification code, and any others are aliases.
     *
     * @return The datum identifiers, or an empty array if there is none.
     * @UML optional datumID
     *
     * @rename  Omitted the "<code>datum</code>" prefix.
     *          Replaced "<code>ID</code>" by "<code>Identifiers</code>" in order to
     *          1) use the return type class name and 2) use the plural form.
     */
    public Identifier[] getIdentifiers();

    /**
     * Description, possibly including coordinates, of the point or points used to anchor the datum
     * to the Earth. Also known as the "origin", especially for Engineering and Image Datums.
     *
     * <ul>
     *   <li>For a geodetic datum, this point is also known as the fundamental point, which is
     *       traditionally the point where the relationship between geoid and ellipsoid is defined.
     *       In some cases, the "fundamental point" may consist of a number of points. In those
     *       cases, the parameters defining the geoid/ellipsoid relationship have then been averaged
     *       for these points, and the averages adopted as the datum definition.</li>
     *
     *   <li>For an engineering datum, the anchor point may be a physical point, or it may be a
     *       point with defined coordinates in another CRS.</li>
     *
     *   <li>For an image datum, the anchor point is usually either the centre of the image or the
     *       corner of the image.</li>
     *
     *   <li>For a temporal datum, this attribute is not defined. Instead of the anchor point,
     *       a temporal datum carries a separate time origin of type {@link Date}.</li>
     * </ul>
     *
     * @return The datum anchor point, or <code>null</code> if not available.
     * @UML optional anchorPoint
     */
    public String getAnchorPoint();

    /**
     * The time after which this datum definition is valid. This time may be precise (e.g. 1997
     * for IRTF97) or merely a year (e.g. 1983 for NAD83). In the latter case, the epoch usually
     * refers to the year in which a major recalculation of the geodetic control network, underlying
     * the datum, was executed or initiated. An old datum can remain valid after a new datum is
     * defined. Alternatively, a datum may be superseded by a later datum, in which case the
     * realization epoch for the new datum defines the upper limit for the validity of the
     * superseded datum.
     *
     * @return The datum realization epoch, or <code>null</code> if not available.
     * @UML optional realizationEpoch
     */
    public Date getRealizationEpoch();

    /**
     * Area or region in which this datum object is valid.
     *
     * @return The datum valid area, or <code>null</code> if not available.
     * @UML optional validArea
     *
     * @revisit The method name <code>getValidExtent()</code> would work better with time
     *          reference systems since their validity holds across a non-spatial extent.
     */
    public Extent getValidArea();

    /**
     * Description of domain of usage, or limitations of usage, for which this
     * datum object is valid.
     *
     * @param  locale The desired locale for the scope to be returned,
     *         or <code>null</code> for a non-localized string (or a default default locale).
     * @return The datum scope, or <code>null</code> if not available.
     * @UML optional scope
     */
    public String getScope(Locale locale);

    /**
     * Comments on or information about this datum, including source information.
     *
     * @param  locale The desired locale for the remarks to be returned,
     *         or <code>null</code> for a non-localized string (or a default default locale).
     * @return The datum remarks, or <code>null</code> if not available.
     * @UML optional remarks
     */
    public String getRemarks(Locale locale);
}
