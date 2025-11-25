class TemplatePromptBuilder:
    template_mining_operation = """You are an expert in mining operations analysis. Here is the sensor output data summary for the unit: {unit_name}.

        Dataset Summary:
        {all_data}

        Based on this data, please provide a few concise, clear, and technically accurate insights describing:
        - Engine performance,
        - Fuel efficiency,
        - Potential operational concerns or anomalies.

        Make sure your insights are contextual and easy to understand for mining operation stakeholders.
        """
