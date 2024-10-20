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
        ],
        "nutrition": {
            "calories": 350,
            "sugar": "20g",
            "protein": "5g",
            "total_fats": "15g",
            "sodium": "200mg"
        }
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
        ],
        "nutrition": {
            "calories": 400,
            "sugar": "25g",
            "protein": "6g",
            "total_fats": "18g",
            "sodium": "220mg"
        }
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
        ],
        "nutrition": {
            "calories": 300,
            "sugar": "18g",
            "protein": "4g",
            "total_fats": "12g",
            "sodium": "180mg"
        }
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
    uvicorn.run(app, host='nathanapi.clowdertech.com', port=8000)
