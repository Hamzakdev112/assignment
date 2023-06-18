{% extends 'base.vue' %}

{% block globalfunctions %}


Vue.component('app', {
  delimiters: ['[[', ']]'],
  template:`
  <div>
    <topbar :openCreatePost="openCreatePost" >></topbar>
    <single-blog v-if="singlePostDialog" :blog="singleBlog" :closeSinglePostDialog="closeSinglePostDialog" :singlePostDialog="singlePostDialog" ></single-blog>
    <edit-blog :fetchBlogs="fetchBlogs" v-if="editPostDialog" :blog="singleBlog" :closeEditPostDialog="closeEditPostDialog " :editPostDialog="editPostDialog" ></edit-blog>
    <create-post-dialog v-if="createPostDialog" :fetchBlogs="fetchBlogs" :closeCreatePostDialog="closeCreatePostDialog" ></create-post-dialog>
    <div class="w-[90%] mx-auto  mt-[20px] ">
      <div v-if="error">
        <span>Some Error Occured</span>
      </div>
      <div v-else>
        <div v-if="isFetching">Loading...</div>
        <div v-else class="flex gap-[20px] flex-wrap justify-center">
          <blog-card :fetchBlogs="fetchBlogs" v-for="(blog) in blogs" :getSingleBlog="getSingleBlog" :openEditPost="openEditPost" :key="blog.id" :blog="blog"></blog-card>
          
        </div>
      </div>
    </div>
</div>
    `,
    data(){
      return {
        blogs:[],
        error:null,
        isFetching:false,
        singleBlog:null,
        singlePostDialog:false,
        editPostDialog:false,
        createPostDialog:false,
      }
    },
    methods:{
      getSingleBlog(blog){
        this.singleBlog = blog
        this.singlePostDialog = true
      },
      closeSinglePostDialog(){
        this.singleBlog = null
        this.singlePostDialog = false
      },
      openEditPost(blog){
        this.singleBlog = blog
        this.editPostDialog = true
      },
      closeEditPostDialog(){
        this.singleBlog = null
        this.editPostDialog = false
      },
      openCreatePost(){
        this.createPostDialog = true
      },
      closeCreatePostDialog(){
        this.createPostDialog = false
      },
      fetchBlogs() {
              this.isFetching = true
              axios
              .get('/api/list')
              .then(response => {
                console.log(response.data)
                this.blogs = response.data
              })
              .catch(error => {
                console.log(error);
                        this.error = error
                    })
                    .finally(()=>this.isFetching = false)
            }
    },
    mounted(){
      this.fetchBlogs()
    },
  })

  Vue.component('topbar', {
    delimiters: ['[[', ']]'],
    template:`
    <nav class="flex items-center justify-center gap-[20px]">
      <h1 class=" text-[2em]">My Blogs</h1>
      <button @click="openCreatePost" class="bg-[blue] text-[white] p-[4px] px-[10px]">Create Post</button>
    </nav>
    `,
    props:{
      openCreatePost:Function,
    }
  })
  
  Vue.component('create-post-dialog', {
    template:`
    <div  class="fixed inset-0 flex items-center z-[11] justify-center bg-gray-900 bg-opacity-50">
      <dialog class="relative dialog w-[400px] bg-white pointer-events-auto" open >
        <button @click="closeCreatePostDialog"  class="absolute top-0 right-0">
          <i class="fa-regular fa-circle-xmark"></i>
        </button>
        <h1 class="text-center text-[1.5em] mb-[5px]">Create Post</h1>
        <div class="p-[5px] flex flex-col gap-[20px]">
            <label class="flex flex-col gap-[5px]">
              Title
              <input v-model="title"  type="text" class="border-[gray] border-[1px]" />
            </label>
            <label class="flex flex-col gap-[5px]">
              Description
              <textarea v-model="body"  class="border-[gray] border-[1px]"></textarea>
            </label>
            <button @click="createPost"  class="bg-[blue] p-[4px] px-[10px] text-[white]">Create</button>
        </div>
      </dialog>
    </div>
    `,
    props:{
      closeCreatePostDialog:Function,
      fetchBlogs:Function
    },
    data(){
      return {
        title:'',
        body:''
      }
    },
    methods:{
      createPost(){
        const body = {title:this.title, body:this.body, published_0:'2023-06-18'}
        axios.post('/api/create/',body)
        .then(({data})=>{
           this.closeCreatePostDialog()
           this.fetchBlogs() 
        })
      }
    }
  })
  

  Vue.component('blog-card', {
  delimiters: ['[[', ']]'],
  template:`
    <div class="relative border-[1px] border-[black] w-[250px] min-h-[100px] flex justify-center items-center flex-col gap-[20px] p-[30px]  overflow-hidden">
      <h1 class="text-[1.5em]">[[blog.title]]</h1>
      <button @click="getSingleBlog(blog)" class="bg-[blue] rounded-[5px] px-[10px] p-[3px] text-[white]">See more</button>
      <div class="absolute top-[2px] right-[5px]">
        <button @click="deletePost(blog.id)" class="text-[#a80909]">
          <i class="fa-solid fa-trash"></i>
        </button>
        <button @click="openEditPost(blog)" class="text-[darkblue]">
          <i class="fa-solid fa-pencil"></i>
        </button>
      </div>
    </div>
  `,
  props: {
    blog: {
        type: Object,
        required: true
    },
    getSingleBlog:{
      type:Function,
    },
    openEditPost:{
      type:Function,
    },
    fetchBlogs:{
      type:Function,
    }
  },
  methods:{
    deletePost(id){
      console.log(id)
      axios.delete(`/api/delete/${id}`).then(()=>{
        this.fetchBlogs()
      })
    }
  }
  })

Vue.component('single-blog', {
  delimiters: ['[[', ']]'],
  props:{
    singlePostDialog:{
      type:Boolean
    },
    blog:{
      type:Object,
      required:true
    },
    closeSinglePostDialog:{
      type:Function
    }
  },
  template:`
  <div class="fixed inset-0 flex items-center z-[11] justify-center bg-gray-900 bg-opacity-50">
    <dialog class=" z-[10] w-[400px] bg-white pointer-events-auto" open>
      <div class="max-w-2xl mx-auto relative">
        <button @click="closeSinglePostDialog" class="absolute top-0 right-0">
          <i class="fa-regular fa-circle-xmark"></i>
        </button>
        <div class="bg-white shadow-md border border-gray-200 rounded-lg max-w-sm dark:bg-gray-800 dark:border-gray-700">
          <!-- <img class="rounded-t-lg" src="https://flowbite.com/docs/images/blog/image-1.jpg" alt=""> -->
      <div class="p-5">
        <h5 class="text-gray-900 font-bold text-2xl tracking-tight mb-2 dark:text-white">[[blog.title]]</h5>
          <p class="font-normal text-gray-700 mb-3 dark:text-gray-400">[[blog.body]]</p>
      </div>
  </div>
</div>
</dialog>
</div>
`
})



Vue.component('edit-blog', {
  delimiters: ['[[', ']]'],
  template:`
  <div v-if="editPostDialog" class="fixed inset-0 flex items-center z-[11] justify-center bg-gray-900 bg-opacity-50">
    <dialog class="relative dialog w-[400px] bg-white pointer-events-auto" open >
      <button @click="closeEditPostDialog" class="absolute top-0 right-0">
        <i class="fa-regular fa-circle-xmark"></i>
      </button>
      <h1 class="text-center text-[1.5em] mb-[5px]">Edit Post</h1>
      <div class="p-[5px] flex flex-col gap-[20px]">
          <label class="flex flex-col gap-[5px]">
            Title
            <input v-model="title" type="text" class="border-[gray] border-[1px]" />
          </label>
          <label class="flex flex-col gap-[5px]">
            Description
            <textarea v-model="body" class="border-[gray] border-[1px]"></textarea>
          </label>
          <button @click="updatePost(blog.id)" class="bg-[blue] p-[4px] px-[10px] text-[white]">Update</button>
      </div>
    </dialog>
  </div>
  `,
  data() {
    return {
      title: '',
      body: '',
    };
  },
  mounted() {
    this.title = this.blog.title;
    this.body = this.blog.body;
  },
  props:{
    editPostDialog:{
      type:Boolean
    },
    blog:{
      type:Object,
      required:true
    },
    closeEditPostDialog:{
      type:Function
    },
    fetchBlogs:{
      type:Function
    },
  },
  methods:{
    updatePost(id){
      const body = {title:this.title, body:this.body}
      axios.put(`/api/update/${id}/`,body)
      .then(()=>{
        this.closeEditPostDialog();
        this.fetchBlogs();
      })
      .catch((error)=>{
        console.log(error)
      })
    }
  },
})


{% endblock globalfunctions %}

  {% block vuescript %}
  
  data: {
  },
  {% endblock vuescript %}