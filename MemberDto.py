from dataclasses import dataclass


@dataclass
class MemberDTO:
    member_type: str
    flat_owner_name: str
    tenant_name: str
    wing_building_no: str
    flat_no: str
    flat_type: str
    primary_contact_no: str
    email_id: str
    owner_contact_no: str
    tenant_contact_no: str
    two_wheelers: int
    four_wheelers: int
    stilt: int
    parking_charges: float
    maintenance_charges: float
    outstanding: float
    maid: bool
    pet: bool
    share_certificate: bool
    remark: str
    key: str  # The 'key' that is provided via request param