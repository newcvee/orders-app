<template>
  <button @click="goToAddCategoryPage">Add Category</button>
  <section class="card" v-for="category in categories" :key="category.category_id">
      <article class="category-card" @click="enterCategory(category)">
          {{category.name}}
          {{category.image}}
      </article>
    <button @click="goToModifyCategoryPage">Modify</button>
  </section>
  {{$data}}
</template>

<script>
import { getCategories } from "@/services/api.js";
export default {
    name: "Categories",
    data(){
        return { 
            categories: {},
            
            };
    },
    mounted() {
        this.loadCategories();
        
    },
    methods: {
        async loadCategories() {
            this.categories = await getCategories();
        },
        
        enterCategory(category){            
         this.$router.push("/category/dishes/" + category.category_id)
        },
        goToAddCategoryPage(){
            this.$router.push("/add-category");

        },
        goToModifyCategoryPage(){
            this.$router.push("/modify-category");
            console.log("Modified")
        }
   

    }
}
</script>

<style>
.card {
    display: inline-block;
    margin: 1%;
    
    }

.category-card {
    width: 30vw;
    height: 30vh;
    border: 1px solid black;
    margin-left: auto;
    margin-right: auto;
}

</style>