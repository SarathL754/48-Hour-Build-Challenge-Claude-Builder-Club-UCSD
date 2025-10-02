from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Innervoiceai():
    """Innervoiceai crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def optimist(self) -> Agent:
        return Agent(
            config=self.agents_config['optimist'],
            verbose=True
        )

    @agent
    def pessimist(self) -> Agent:
        return Agent(
            config=self.agents_config['pessimist'],
            verbose=True
        )
    @agent
    def ethicist(self) -> Agent:
        return Agent(
            config=self.agents_config['ethicist'],
            verbose=True
        )
    @agent
    def mediator(self) -> Agent:
        return Agent(
            config=self.agents_config['mediator'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def evaluate_from_optimist(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_from_optimist'],
        )

    @task
    def evaluate_from_pessimist(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_from_pessimist'],
        )
    
    @task
    def evaluate_from_ethics(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_from_ethics'],
        )
    
    @task
    def mediate_and_recommend(self) -> Task:
        return Task(
            config=self.tasks_config['mediate_and_recommend'],
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Innervoiceai crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
