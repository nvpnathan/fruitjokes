import Recipe from "../Recipe";
import React, {useState} from "react";
import PopupModal from "../Modal/PopupModal";
import FormInput from "../FormInput/FormInput";

const RecipeTable = ({jokes}) => {

  const [recipeInfoModal, setRecipeInfoModal] = useState(false)

    return (
      <>
        <div className="sections-list">
          {jokes.length && (
              jokes.map((joke) => (
                <Recipe showRecipeInfoModal={() => setRecipeInfoModal(joke)} key={joke.id} joke={joke}  />
              ))
          )}
          {!jokes.length && (
              <p>No jokes found!</p>
          )}
        </div>
        {recipeInfoModal && <PopupModal
						modalTitle={"Recipe Info"}
						onCloseBtnPress={() => {
							setRecipeInfoModal(false);
						}}
					>
						<div className="mt-4 text-left">
							<form className="mt-5">
								<FormInput
									disabled
									type={"text"}
									name={"label"}
									label={"Label"}
									value={recipeInfoModal?.label}
								/>
								<FormInput
									disabled
									type={"text"}
									name={"url"}
									label={"Url"}
									value={recipeInfoModal?.url}
								/>
								<FormInput
									disabled
									type={"text"}
									name={"source"}
									label={"Source"}
									value={recipeInfoModal?.source}
								/>
							</form>
						</div>
					</PopupModal>}
      </>
    )
}

export default RecipeTable;