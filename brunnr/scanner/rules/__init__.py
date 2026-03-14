"""Rule registry — default rule set.

Order matches the original scan_skill_md() execution order.
"""

from brunnr.scanner.rules.cmd_injection import CommandInjectionRule
from brunnr.scanner.rules.cred_theft import CredentialTheftRule
from brunnr.scanner.rules.data_exfil import DataExfiltrationRule
from brunnr.scanner.rules.keyword_divergence import KeywordDivergenceRule
from brunnr.scanner.rules.priv_esc import PrivilegeEscalationRule
from brunnr.scanner.rules.prompt_override import PromptOverrideRule
from brunnr.scanner.rules.sensitive_paths import SensitivePathRule
from brunnr.scanner.rules.steg_patterns import StegPatternRule
from brunnr.scanner.rules.supply_chain import SupplyChainRule
from brunnr.scanner.rules.url_domains import UrlDomainRule
from brunnr.scanner.rules.zero_width import ZeroWidthRule

DEFAULT_RULES: list[type[object]] = [
    CommandInjectionRule,
    DataExfiltrationRule,
    CredentialTheftRule,
    PromptOverrideRule,
    SupplyChainRule,
    PrivilegeEscalationRule,
    ZeroWidthRule,
    StegPatternRule,
    UrlDomainRule,
    SensitivePathRule,
    KeywordDivergenceRule,
]
