import os
import shutil

from graph.state import PipelineState


class BronzeAgent:

    def execute(self, state: PipelineState):

        os.makedirs("data/bronze", exist_ok=True)

        destination = os.path.join(
            "data",
            "bronze",
            os.path.basename(state.source_file)
        )

        shutil.copy2(state.source_file, destination)

        state.recommendations.append(
            f"Bronze layer created: {destination}"
        )

        return state