# Imports
import pickle

from problem_formulation import get_model_for_problem_formulation

from ema_workbench.em_framework.optimization import EpsilonProgress, ArchiveLogger, to_problem, epsilon_nondominated

from ema_workbench import ema_logging, ScalarOutcome, SequentialEvaluator
from ema_workbench.em_framework.evaluators import BaseEvaluator



if __name__ == '__main__':
    
    ema_logging.log_to_stderr(ema_logging.INFO)
    
    # Get model and scenarios
    dike_model, planning_steps = get_model_for_problem_formulation(6)
    
    # Relevant outcomes are set to minimized
    dike_model.outcomes = [ScalarOutcome("A.2_Expected Annual Damage", kind=ScalarOutcome.MINIMIZE, function=sum),
                       ScalarOutcome("A.2_Expected Number of Deaths", kind=ScalarOutcome.MINIMIZE, function=sum),
                       ScalarOutcome("A.2_Dike Investment Costs", kind=ScalarOutcome.MINIMIZE, function=sum),
                       ScalarOutcome("RfR Total Costs", kind=ScalarOutcome.MINIMIZE, function=sum)]

    # From an external scenario file, the scenarios are loaded in
    scenario_file = open('scenarioList', 'rb')
    scenario_list = pickle.load(scenario_file)
    scenario_file.close()

    # As explained in the discussion, we couldn't get the Multi processing or MPI evaluator to run
    # That's why this script is run seperately for each scenario, and why the specific scenario is chosen below
    scenario = scenario_list[0]

    ema_logging.log_to_stderr(ema_logging.INFO)

    def optimize(scenario, nfe, model, epsilons):
        results = []
        convergences = []
        problem = to_problem(model, searchover="levers")

        with SequentialEvaluator(dike_model) as evaluator:
            # The model is run for 3 seeds per scenario
            # Convergence metrics are saved using ArchiveLogger from the EMA Workbench
            for i in range(3):
                convergence_metrics = [
                    ArchiveLogger(
                        "./archives",
                        [l.name for l in model.levers],
                        [o.name for o in model.outcomes],
                        base_filename=f"{scenario.name}_seed_{i}.tar.gz",
                    ),
                    EpsilonProgress(),
                ]

                # Searched over levers, as we want policies as results
                result, convergence = evaluator.optimize(nfe=nfe, searchover='levers',
                                            convergence=convergence_metrics,
                                            epsilons=epsilons,
                                            reference=scenario)

                # Save the results and convergence data to the list for each seed 
                results.append(result)
                convergences.append(convergence)
        
        reference_set = results
        
        # Returns the results and convergence data of one scenario
        return reference_set, convergences


    results = []
    # Epsilon values for all costs are 1000, 0.25 is used for deaths as the related outcomes is generally much smaller
    epsilons = [1000, 1000, 0.25, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    results.append(optimize(scenario, 100000, dike_model, epsilons))


    # Save results
    results_file = open('resultsFile', 'wb')
    pickle.dump(results, results_file)
    results_file.close()