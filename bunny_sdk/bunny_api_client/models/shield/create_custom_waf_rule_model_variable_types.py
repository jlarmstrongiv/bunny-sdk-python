from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CreateCustomWafRuleModel_variableTypes(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ARGS property
    a_r_g_s: Optional[str] = None
    # The ARGS_COMBINED_SIZE property
    a_r_g_s_c_o_m_b_i_n_e_d_s_i_z_e: Optional[str] = None
    # The ARGS_GET property
    a_r_g_s_g_e_t: Optional[str] = None
    # The ARGS_GET_NAMES property
    a_r_g_s_g_e_t_n_a_m_e_s: Optional[str] = None
    # The ARGS_POST property
    a_r_g_s_p_o_s_t: Optional[str] = None
    # The ARGS_POST_NAMES property
    a_r_g_s_p_o_s_t_n_a_m_e_s: Optional[str] = None
    # The FILES_NAMES property
    f_i_l_e_s_n_a_m_e_s: Optional[str] = None
    # The GEO property
    g_e_o: Optional[str] = None
    # The QUERY_STRING property
    q_u_e_r_y_s_t_r_i_n_g: Optional[str] = None
    # The REMOTE_ADDR property
    r_e_m_o_t_e_a_d_d_r: Optional[str] = None
    # The REQUEST_BASENAME property
    r_e_q_u_e_s_t_b_a_s_e_n_a_m_e: Optional[str] = None
    # The REQUEST_BODY property
    r_e_q_u_e_s_t_b_o_d_y: Optional[str] = None
    # The REQUEST_COOKIES property
    r_e_q_u_e_s_t_c_o_o_k_i_e_s: Optional[str] = None
    # The REQUEST_COOKIES_NAMES property
    r_e_q_u_e_s_t_c_o_o_k_i_e_s_n_a_m_e_s: Optional[str] = None
    # The REQUEST_FILENAME property
    r_e_q_u_e_s_t_f_i_l_e_n_a_m_e: Optional[str] = None
    # The REQUEST_HEADERS property
    r_e_q_u_e_s_t_h_e_a_d_e_r_s: Optional[str] = None
    # The REQUEST_HEADERS_NAMES property
    r_e_q_u_e_s_t_h_e_a_d_e_r_s_n_a_m_e_s: Optional[str] = None
    # The REQUEST_LINE property
    r_e_q_u_e_s_t_l_i_n_e: Optional[str] = None
    # The REQUEST_METHOD property
    r_e_q_u_e_s_t_m_e_t_h_o_d: Optional[str] = None
    # The REQUEST_PROTOCOL property
    r_e_q_u_e_s_t_p_r_o_t_o_c_o_l: Optional[str] = None
    # The REQUEST_URI property
    r_e_q_u_e_s_t_u_r_i: Optional[str] = None
    # The REQUEST_URI_RAW property
    r_e_q_u_e_s_t_u_r_i_r_a_w: Optional[str] = None
    # The RESPONSE_BODY property
    r_e_s_p_o_n_s_e_b_o_d_y: Optional[str] = None
    # The RESPONSE_HEADERS property
    r_e_s_p_o_n_s_e_h_e_a_d_e_r_s: Optional[str] = None
    # The RESPONSE_STATUS property
    r_e_s_p_o_n_s_e_s_t_a_t_u_s: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateCustomWafRuleModel_variableTypes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateCustomWafRuleModel_variableTypes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateCustomWafRuleModel_variableTypes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ARGS": lambda n : setattr(self, 'a_r_g_s', n.get_str_value()),
            "ARGS_COMBINED_SIZE": lambda n : setattr(self, 'a_r_g_s_c_o_m_b_i_n_e_d_s_i_z_e', n.get_str_value()),
            "ARGS_GET": lambda n : setattr(self, 'a_r_g_s_g_e_t', n.get_str_value()),
            "ARGS_GET_NAMES": lambda n : setattr(self, 'a_r_g_s_g_e_t_n_a_m_e_s', n.get_str_value()),
            "ARGS_POST": lambda n : setattr(self, 'a_r_g_s_p_o_s_t', n.get_str_value()),
            "ARGS_POST_NAMES": lambda n : setattr(self, 'a_r_g_s_p_o_s_t_n_a_m_e_s', n.get_str_value()),
            "FILES_NAMES": lambda n : setattr(self, 'f_i_l_e_s_n_a_m_e_s', n.get_str_value()),
            "GEO": lambda n : setattr(self, 'g_e_o', n.get_str_value()),
            "QUERY_STRING": lambda n : setattr(self, 'q_u_e_r_y_s_t_r_i_n_g', n.get_str_value()),
            "REMOTE_ADDR": lambda n : setattr(self, 'r_e_m_o_t_e_a_d_d_r', n.get_str_value()),
            "REQUEST_BASENAME": lambda n : setattr(self, 'r_e_q_u_e_s_t_b_a_s_e_n_a_m_e', n.get_str_value()),
            "REQUEST_BODY": lambda n : setattr(self, 'r_e_q_u_e_s_t_b_o_d_y', n.get_str_value()),
            "REQUEST_COOKIES": lambda n : setattr(self, 'r_e_q_u_e_s_t_c_o_o_k_i_e_s', n.get_str_value()),
            "REQUEST_COOKIES_NAMES": lambda n : setattr(self, 'r_e_q_u_e_s_t_c_o_o_k_i_e_s_n_a_m_e_s', n.get_str_value()),
            "REQUEST_FILENAME": lambda n : setattr(self, 'r_e_q_u_e_s_t_f_i_l_e_n_a_m_e', n.get_str_value()),
            "REQUEST_HEADERS": lambda n : setattr(self, 'r_e_q_u_e_s_t_h_e_a_d_e_r_s', n.get_str_value()),
            "REQUEST_HEADERS_NAMES": lambda n : setattr(self, 'r_e_q_u_e_s_t_h_e_a_d_e_r_s_n_a_m_e_s', n.get_str_value()),
            "REQUEST_LINE": lambda n : setattr(self, 'r_e_q_u_e_s_t_l_i_n_e', n.get_str_value()),
            "REQUEST_METHOD": lambda n : setattr(self, 'r_e_q_u_e_s_t_m_e_t_h_o_d', n.get_str_value()),
            "REQUEST_PROTOCOL": lambda n : setattr(self, 'r_e_q_u_e_s_t_p_r_o_t_o_c_o_l', n.get_str_value()),
            "REQUEST_URI": lambda n : setattr(self, 'r_e_q_u_e_s_t_u_r_i', n.get_str_value()),
            "REQUEST_URI_RAW": lambda n : setattr(self, 'r_e_q_u_e_s_t_u_r_i_r_a_w', n.get_str_value()),
            "RESPONSE_BODY": lambda n : setattr(self, 'r_e_s_p_o_n_s_e_b_o_d_y', n.get_str_value()),
            "RESPONSE_HEADERS": lambda n : setattr(self, 'r_e_s_p_o_n_s_e_h_e_a_d_e_r_s', n.get_str_value()),
            "RESPONSE_STATUS": lambda n : setattr(self, 'r_e_s_p_o_n_s_e_s_t_a_t_u_s', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("ARGS", self.a_r_g_s)
        writer.write_str_value("ARGS_COMBINED_SIZE", self.a_r_g_s_c_o_m_b_i_n_e_d_s_i_z_e)
        writer.write_str_value("ARGS_GET", self.a_r_g_s_g_e_t)
        writer.write_str_value("ARGS_GET_NAMES", self.a_r_g_s_g_e_t_n_a_m_e_s)
        writer.write_str_value("ARGS_POST", self.a_r_g_s_p_o_s_t)
        writer.write_str_value("ARGS_POST_NAMES", self.a_r_g_s_p_o_s_t_n_a_m_e_s)
        writer.write_str_value("FILES_NAMES", self.f_i_l_e_s_n_a_m_e_s)
        writer.write_str_value("GEO", self.g_e_o)
        writer.write_str_value("QUERY_STRING", self.q_u_e_r_y_s_t_r_i_n_g)
        writer.write_str_value("REMOTE_ADDR", self.r_e_m_o_t_e_a_d_d_r)
        writer.write_str_value("REQUEST_BASENAME", self.r_e_q_u_e_s_t_b_a_s_e_n_a_m_e)
        writer.write_str_value("REQUEST_BODY", self.r_e_q_u_e_s_t_b_o_d_y)
        writer.write_str_value("REQUEST_COOKIES", self.r_e_q_u_e_s_t_c_o_o_k_i_e_s)
        writer.write_str_value("REQUEST_COOKIES_NAMES", self.r_e_q_u_e_s_t_c_o_o_k_i_e_s_n_a_m_e_s)
        writer.write_str_value("REQUEST_FILENAME", self.r_e_q_u_e_s_t_f_i_l_e_n_a_m_e)
        writer.write_str_value("REQUEST_HEADERS", self.r_e_q_u_e_s_t_h_e_a_d_e_r_s)
        writer.write_str_value("REQUEST_HEADERS_NAMES", self.r_e_q_u_e_s_t_h_e_a_d_e_r_s_n_a_m_e_s)
        writer.write_str_value("REQUEST_LINE", self.r_e_q_u_e_s_t_l_i_n_e)
        writer.write_str_value("REQUEST_METHOD", self.r_e_q_u_e_s_t_m_e_t_h_o_d)
        writer.write_str_value("REQUEST_PROTOCOL", self.r_e_q_u_e_s_t_p_r_o_t_o_c_o_l)
        writer.write_str_value("REQUEST_URI", self.r_e_q_u_e_s_t_u_r_i)
        writer.write_str_value("REQUEST_URI_RAW", self.r_e_q_u_e_s_t_u_r_i_r_a_w)
        writer.write_str_value("RESPONSE_BODY", self.r_e_s_p_o_n_s_e_b_o_d_y)
        writer.write_str_value("RESPONSE_HEADERS", self.r_e_s_p_o_n_s_e_h_e_a_d_e_r_s)
        writer.write_str_value("RESPONSE_STATUS", self.r_e_s_p_o_n_s_e_s_t_a_t_u_s)
        writer.write_additional_data_value(self.additional_data)
    

