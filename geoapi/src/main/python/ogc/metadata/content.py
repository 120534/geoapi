#
#    GeoAPI - Programming interfaces for OGC/ISO standards
#    http://www.geoapi.org
#
#    Copyright (C) 2018 Open Geospatial Consortium, Inc.
#    All Rights Reserved. http://www.opengeospatial.org/ogc/legal
#

from abc import ABC, abstractproperty
from typing import Sequence
from enum import Enum



class BandDefinition(Enum):
    THREE_DB = "3dB"
    HALF_MAXIMUM = "halfMaximum"
    FIFTY_PERCENT = "fiftyPercent"
    ONE_OVER_E = "oneOverE"
    EQUIVALENT_WIDTH = "equivalentWidth"



class CoverageContentTypeCode(Enum):
    IMAGE = "image"
    THEMATIC_CLASSIFICATION = "thematicClassification"
    PHYSICAL_MEASUREMENT = "physicalMeasurement"
    AUXILLARY_INFORMATION = "auxillaryInformation"
    QUALITY_INFORMATION = "qualityInformation"
    REFERENCE_INFORMATION = "referenceInformation"
    MODEL_RESULT = "modelResult"
    COORDINATE = "coordinate"



class ImagingConditionCode(Enum):
    BLURRED_IMAGE = "blurredImage"
    CLOUD = "cloud"
    DEGRADING_OBLIQUITY = "degradingObliquity"
    FOG = "fog"
    HEAVY_SMOKE_OR_DUST = "heavySmokeOrDust"
    NIGHT = "night"
    RAIN = "rain"
    SEMI_DARKNESS = "semiDarkness"
    SHADOW = "shadow"
    SNOW = "snow"
    TERRAIN_MASKING = "terrainMasking"



class PolarizationOrientationCode(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    LEFT_CIRCULAR = "leftCircular"
    RIGHT_CIRCULAR = "rightCircular"
    THETA = "theta"
    PHI = "phi"



class TransferFunctionTypeCode(Enum):
    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"
    EXPONENTIAL = "exponential"



from ogc.metadata.naming import MemberName, RecordType, Record, GenericName
from ogc.metadata.citation import Identifier, Citation

class RangeDimension(ABC):
    """Information on the range of attribute values."""

    @property
    def sequenceIdentifier(self) -> MemberName:
        """Number that uniquely identifies instances of bands of wavelengths on which a sensor operates."""
        return None

    @property
    def description(self) -> str:
        """Description of the range of a cell measurement value."""
        return None

    @property
    def name(self) -> Sequence[Identifier]:
        """Identifiers for each attribute included in the resource. These identifiers can be used to provide names for the resource's attribute from a standard set of names."""
        return None



class AttributeGroup(ABC):

    @abstractproperty
    def contentType(self) -> Sequence[CoverageContentTypeCode]:
        """Type of information represented by the value."""
        pass

    @property
    def attribute(self) -> Sequence[RangeDimension]:
        return None



class SampleDimension(RangeDimension):
    """The characteristics of each dimension (layer) included in the resource."""

    @property
    def maxValue(self) -> float:
        """Maximum value of data values in each dimension included in the resource. Restricted to UomLength in the MD_Band class."""
        return None

    @property
    def minValue(self) -> float:
        """Minimum value of data values in each dimension included in the resource. Restricted to UomLength in the MD_Band class."""
        return None

    @property
    def units(self):
        """Units of data in each dimension included in the resource. Note that the type of this is UnitOfMeasure and that it is restricted to UomLength in the MD_Band class."""
        return None

    @property
    def scaleFactor(self) -> float:
        """Scale factor which has been applied to the cell value."""
        return None

    @property
    def offset(self) -> float:
        """The physical value corresponding to a cell value of zero."""
        return None

    @property
    def meanValue(self) -> float:
        """Mean value of data values in each dimension included in the resource."""
        return None

    @property
    def numberOfValues(self) -> int:
        """This gives the number of values used in a thematicClassification resource EX:. the number of classes in a Land Cover Type coverage or the number of cells with data in other types of coverages."""
        return None

    @property
    def standardDeviation(self) -> float:
        """Standard deviation of data values in each dimension included in the resource."""
        return None

    @property
    def otherPropertyType(self) -> RecordType:
        """Type of other attribute description (i.e. netcdf/variable in ncml.xsd)."""
        return None

    @property
    def otherProperty(self) -> Record:
        """Instance of otherAttributeType that defines attributes not explicitly included in MD_CoverageType."""
        return None

    @property
    def bitsPerValue(self) -> int:
        """Maximum number of significant bits in the uncompressed representation for the value in each band of each pixel."""
        return None

    @property
    def transferFunctionType(self) -> TransferFunctionTypeCode:
        return None

    @property
    def nominalSpatialResolution(self) -> float:
        return None



class Band(SampleDimension):
    """Range of wavelengths in the electromagnetic spectrum."""

    @property
    def boundMax(self) -> float:
        return None

    @property
    def boundMin(self) -> float:
        return None

    @property
    def boundUnits(self):
        return None

    @property
    def peakResponse(self) -> float:
        """Wavelength at which the response is the highest."""
        return None

    @property
    def toneGradation(self) -> int:
        """Number of discrete numerical values in the grid data."""
        return None

    @property
    def bandBoundaryDefinition(self) -> BandDefinition:
        """Designation of criterion for defining maximum and minimum wavelengths for a spectral band."""
        return None

    @property
    def detectedPolarization(self) -> PolarizationOrientationCode:
        return None

    @property
    def transmittedPolarization(self) -> PolarizationOrientationCode:
        return None



class ContentInformation(ABC):
    """Description of the content of a resource."""



class RangeElementDescription(ABC):
    """Description of specific range elements."""

    @abstractproperty
    def name(self) -> str:
        """Designation associated with a set of range elements."""
        pass

    @abstractproperty
    def definition(self) -> str:
        """Description of a set of specific range elements."""
        pass

    @abstractproperty
    def rangeElement(self) -> Sequence[Record]:
        """Specific range elements, i.e. range elements associated with a name and definition defining their meaning."""
        pass



class CoverageDescription(ContentInformation):
    """Details about the content of a resource."""

    @abstractproperty
    def attributeDescription(self) -> RecordType:
        """Description of the attribute described by the measurement value."""
        pass

    @property
    def processingLevelCode(self) -> Identifier:
        """Code and codespace that identifies the level of processing that has been applied to the resource."""
        return None

    @property
    def attributeGroup(self) -> Sequence[AttributeGroup]:
        return None

    @property
    def rangeElementDescription(self) -> Sequence[RangeElementDescription]:
        return None



class ImageDescription(CoverageDescription):
    """Information about an image's suitability for use."""

    @property
    def illuminationElevationAngle(self) -> float:
        """Illumination elevation measured in degrees clockwise from the target plane at intersection of the optical line of sight with the Earth's surface. For images from a scanning device, refer to the centre pixel of the image."""
        return None

    @property
    def illuminationAzimuthAngle(self) -> float:
        """Illumination azimuth measured in degrees clockwise from true north at the time the image is taken. For images from a scanning device, refer to the centre pixel of the image."""
        return None

    @property
    def imagingCondition(self) -> ImagingConditionCode:
        """Conditions affected the image."""
        return None

    @property
    def imageQualityCode(self) -> Identifier:
        """Code in producers code space that specifies the image quality."""
        return None

    @property
    def cloudCoverPercentage(self) -> float:
        """Area of the dataset obscured by clouds, expressed as a percentage of the spatial extent."""
        return None

    @property
    def compressionGenerationQuantity(self) -> int:
        """Count of the number of lossy compression cycles performed on the image."""
        return None

    @property
    def triangulationIndicator(self):
        """Indication of whether or not triangulation has been performed upon the image."""
        return None

    @property
    def radiometricCalibrationDataAvailability(self):
        """Indication of whether or not the radiometric calibration information for generating the radiometrically calibrated standard data product is available."""
        return None

    @property
    def cameraCalibrationInformationAvailability(self):
        """Indication of whether or not constants are available which allow for camera calibration corrections."""
        return None

    @property
    def filmDistortionInformationAvailability(self):
        """Indication of whether or not Calibration Reseau information is available."""
        return None

    @property
    def lensDistortionInformationAvailability(self):
        """Indication of whether or not lens aberration correction information is available."""
        return None



class FeatureTypeInfo(ABC):

    @abstractproperty
    def featureTypeName(self) -> GenericName:
        pass

    @property
    def featureInstanceCount(self) -> int:
        return None



class FeatureCatalogueDescription(ContentInformation):
    """Information identifying the feature catalogue or the conceptual schema."""

    @property
    def complianceCode(self):
        """Indication of whether or not the cited feature catalogue complies with ISO 19110."""
        return None

    @property
    def locale(self):
        """Language(s) used within the catalogue."""
        return None

    @property
    def includedWithDataset(self):
        """Indication of whether or not the feature catalogue is included with the resource."""
        return None

    @property
    def featureTypes(self) -> Sequence[FeatureTypeInfo]:
        """Subset of feature types from cited feature catalogue occurring in dataset."""
        return None

    @property
    def featureCatalogueCitation(self) -> Sequence[Citation]:
        """Complete bibliographic reference to one or more external feature catalogues."""
        return None
