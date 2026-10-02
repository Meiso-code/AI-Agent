class Agent:
    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        self.name = name
        self.model = model

    def run(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def think(self, message: str) -> str:
        return f"Thinking about: {message}"


# --- FINANCIAL COMPANY AGENTS ---

class FinancialAgent(Agent):
    def __init__(self, name: str, model: str = "gpt-4o-mini", speciality: str = "general"):
        super().__init__(name, model)
        self.speciality = speciality


class RiskAnalysisAgent(FinancialAgent):
    def __init__(self, name: str = "RiskAnalyzer", model: str = "gpt-4o-mini"):
        super().__init__(name, model, speciality="risk_analysis")

    def run(self, message: str) -> str:
        return f"[Risk Analysis] Evaluating: {message}\n-> Assessing market risk, credit risk, operational risk\n-> Calculating risk metrics and recommendations"


class InvestmentAnalysisAgent(FinancialAgent):
    def __init__(self, name: str = "InvestmentAnalyzer", model: str = "gpt-4o-mini"):
        super().__init__(name, model, speciality="investment_analysis")

    def run(self, message: str) -> str:
        return f"[Investment Analysis] Analyzing: {message}\n-> Reviewing financial statements\n-> Evaluating asset performance\n-> Generating investment recommendations"


class ComplianceAgent(FinancialAgent):
    def __init__(self, name: str = "ComplianceOfficer", model: str = "gpt-4o-mini"):
        super().__init__(name, model, speciality="compliance")

    def run(self, message: str) -> str:
        return f"[Compliance] Checking: {message}\n-> Verifying regulatory requirements\n-> Ensuring policy adherence\n-> Flagging compliance issues"


class PortfolioManagementAgent(FinancialAgent):
    def __init__(self, name: str = "PortfolioManager", model: str = "gpt-4o-mini"):
        super().__init__(name, model, speciality="portfolio_management")

    def run(self, message: str) -> str:
        return f"[Portfolio Management] Optimizing: {message}\n-> Asset allocation analysis\n-> Risk-return profiling\n-> Rebalancing recommendations"


class MarketResearchAgent(FinancialAgent):
    def __init__(self, name: str = "MarketResearcher", model: str = "gpt-4o-mini"):
        super().__init__(name, model, speciality="market_research")

    def run(self, message: str) -> str:
        return f"[Market Research] Investigating: {message}\n-> Industry trends analysis\n-> Competitive landscape\n-> Economic indicators"


# --- CONTENT PRODUCTION COMPANY AGENTS ---

class ContentAgent(Agent):
    def __init__(self, name: str, model: str = "gpt-4o-mini", content_type: str = "general"):
        super().__init__(name, model)
        self.content_type = content_type


class ContentStrategyAgent(ContentAgent):
    def __init__(self, name: str = "ContentStrategist", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="strategy")

    def run(self, message: str) -> str:
        return f"[Content Strategy] Planning: {message}\n-> Audience analysis\n-> Content pillars definition\n-> Channel strategy\n-> ROI metrics setup"


class ContentCreationAgent(ContentAgent):
    def __init__(self, name: str = "ContentCreator", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="creation")

    def run(self, message: str) -> str:
        return f"[Content Creation] Producing: {message}\n-> Drafting article/video/script\n-> Research phase\n-> Original content generation"


class EditingAgent(ContentAgent):
    def __init__(self, name: str = "ContentEditor", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="editing")

    def run(self, message: str) -> str:
        return f"[Editing] Refining: {message}\n-> Grammar and style check\n-> Fact-verification\n-> Tone and brand alignment\n-> Final polish"


class SEOOptimizationAgent(ContentAgent):
    def __init__(self, name: str = "SEO specialist", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="seo")

    def run(self, message: str) -> str:
        return f"[SEO Optimization] Optimizing: {message}\n-> Keyword research\n-> On-page SEO elements\n-> Meta data optimization\n-> Readability and structure"


class DistributionAgent(ContentAgent):
    def __init__(self, name: str = "ContentDistributor", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="distribution")

    def run(self, message: str) -> str:
        return f"[Distribution] Publishing: {message}\n-> Platform selection\n-> Scheduling calendar\n-> Multi-channel syndication\n-> Audience targeting"


class AnalyticsAgent(ContentAgent):
    def __init__(self, name: str = "ContentAnalyst", model: str = "gpt-4o-mini"):
        super().__init__(name, model, content_type="analytics")

    def run(self, message: str) -> str:
        return f"[Analytics] Measuring: {message}\n-> Performance metrics tracking\n-> Audience engagement analysis\n-> Content ROI calculation\n-> Strategy adjustment recommendations"


# --- COMPOSITE ORGANIZATIONAL AGENTS ---

class FinancialInstitute:
    def __init__(self, name: str):
        self.name = name
        self.risk_agent = RiskAnalysisAgent(f"{name}_Risk")
        self.investment_agent = InvestmentAnalysisAgent(f"{name}_Investment")
        self.compliance_agent = ComplianceAgent(f"{name}_Compliance")
        self.portfolio_agent = PortfolioManagementAgent(f"{name}_Portfolio")
        self.market_agent = MarketResearchAgent(f"{name}_Market")

    def analyze_opportunity(self, opportunity: str) -> str:
        results = []
        results.append(self.risk_agent.run(opportunity))
        results.append(self.investment_agent.run(opportunity))
        results.append(self.compliance_agent.run(opportunity))
        results.append(self.portfolio_agent.run(opportunity))
        results.append(self.market_agent.run(opportunity))
        return "\n\n".join(results)


class ContentProductionHouse:
    def __init__(self, name: str):
        self.name = name
        self.strategy_agent = ContentStrategyAgent(f"{name}_Strategy")
        self.creation_agent = ContentCreationAgent(f"{name}_Creation")
        self.editing_agent = EditingAgent(f"{name}_Editing")
        self.seo_agent = SEOOptimizationAgent(f"{name}_SEO")
        self.distribution_agent = DistributionAgent(f"{name}_Distribution")
        self.analytics_agent = AnalyticsAgent(f"{name}_Analytics")

    def produce_content(self, topic: str) -> str:
        results = []
        results.append(self.strategy_agent.run(topic))
        results.append(self.creation_agent.run(topic))
        results.append(self.editing_agent.run(topic))
        results.append(self.seo_agent.run(topic))
        results.append(self.distribution_agent.run(topic))
        results.append(self.analytics_agent.run(topic))
        return "\n\n".join(results)