from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

recipes = {
    "blueberry_muffin": {
        "ingredients": [
            "1 cup blueberries",
            "2 cups flour",
            "1 cup sugar",
            "1/2 cup milk",
            "1/2 cup butter",
            "2 eggs",
            "1 tsp baking powder",
            "1 tsp vanilla extract"
        ],
        "instructions": [
            "Preheat oven to 375°F.",
            "Mix dry ingredients.",
            "Mix wet ingredients.",
            "Combine and fold in blueberries.",
            "Bake for 20-25 minutes."
        ]
    },
    "chocolate_muffin": {
        "ingredients": [
            "1 cup cocoa powder",
            "2 cups flour",
            "1 cup sugar",
            "1 cup milk",
            "1/2 cup butter",
            "2 eggs",
            "1 tsp baking powder",
            "1 tsp vanilla extract"
        ],
        "instructions": [
            "Preheat oven to 375°F.",
            "Mix dry ingredients.",
            "Mix wet ingredients.",
            "Combine.",
            "Bake for 20-25 minutes."
        ]
    },
    "banana_bread": {
        "ingredients": [
            "3 ripe bananas",
            "2 cups flour",
            "1 cup sugar",
            "1/2 cup milk",
            "1/2 cup butter",
            "2 eggs",
            "1 tsp baking powder",
            "1 tsp vanilla extract"
        ],
        "instructions": [
            "Preheat oven to 375°F.",
            "Mash bananas.",
            "Mix dry ingredients.",
            "Mix wet ingredients.",
            "Combine.",
            "Bake for 20-25 minutes."
        ]
    }
}

@app.get('/bakedgoods/{item_type}')
async def get_baked_good(item_type: str):
    recipe = recipes.get(item_type.lower())
    if recipe:
        return JSONResponse(content=recipe)
    else:
        raise HTTPException(status_code=404, detail="Baked good not found")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
