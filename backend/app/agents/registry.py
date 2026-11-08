from dataclasses import dataclass
@dataclass(frozen=True)
class AgentDefinition:
    name: str
    purpose: str
    prompt_file: str
AGENTS = {
    "intelligence": AgentDefinition("intelligence", "Market and competitor research", "intelligence.md"),
    "affiliate": AgentDefinition("affiliate", "Affiliate programme and product evaluation", "affiliate.md"),
    "strategist": AgentDefinition("strategist", "Audience and campaign strategy", "strategist.md"),
    "content": AgentDefinition("content", "Multi-channel content drafting", "content.md"),
    "creative": AgentDefinition("creative", "Advertising creative briefs", "creative.md"),
    "compliance": AgentDefinition("compliance", "Claims, disclosures and policy checks", "compliance.md"),
    "growth": AgentDefinition("growth", "Performance analysis and experiments", "growth.md"),
    "acquisition": AgentDefinition("acquisition", "Agency prospect research and proposals", "acquisition.md"),
}
