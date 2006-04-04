package org.opengis.feature;

import org.opengis.feature.type.AssociationDescriptor;
import org.opengis.feature.type.AssociationType;
import org.opengis.feature.type.AttributeType;

/**
 * Contains information defining an associated attribtue (ie shared value).
 * <p>
 * An Association is used to hold a relation in our data model, similar to the
 * way a Key is used to Associatte a Value in a Map. Rather then use Map.Entry
 * to capture this link we are using a strongly typed AssociationType providing
 * additional information indicating the nature of the association.
 * </p>
 * <p>
 * If this Association is contained in another data sturcutre you may use the
 * provided AssociationDescriptor. This descriptor will provided any additional
 * information (such as name and multiplicity) needed.
 * </p>
 * 
 * @author Jody Garnett, Refractions Research
 */
public interface Association<B,T extends AttributeType<B>,A extends AssociationType<T>> extends Property<T> {

	/**
	 * Indicates the AttirbuteDescriptor for this content.
	 * <p>
	 * The attribute descriptor formally captures the name and multiplicity
	 * information for this attribute. If this attribute is not contained in a
	 * container, then the descriptor will be null.
	 * </p>
	 * 
	 * @return Descriptor for this attribute, may be null.
	 */
	AssociationDescriptor<T> getDescriptor();

	/**
	 * Indicate the AssociationType, if we have a descriptor it will be in
	 * agreement.
	 * <p>
	 * This information indicates the nature of the relationship captured by this assocation.
	 * At a minimum the following categories shoul dbe thought about aggregation (ie member of
	 * shared), temporal (before after ) or spatial (contained, touches).
	 * @return AttributeType information descirbing allowable content
	 */
	T getType();
	
	/**
	 * Indicates the AttributeType we are associated with.
	 * <p>
	 * Note the target attirbute type is likely maintained in another part of the
	 * forest, often it will be fetched via either a query or optimally by ID lookup
	 * behind the scenes.
	 * </p>
	 * @return type of attribute we are related to.
	 */
	A getAssociateType();
	
	/**
	 * An associated Attribute.
	 * <p>
	 * This will be of the type indicated by the getAssociateType.
	 * 
	 * @return associated attribtue
	 */
	Attribute<B,T> getAssociate();
	
	/**
	 * Set the association to the provided Attribute
	 * @param value
	 */
	void setAssociate(Attribute<B,V> value );
}