<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text">
                <h2>Create Task</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Title</label>
                                <div class="col-sm-6 align=left">
                                    <input type="text" placeholder="Title" name="title" class="form-control">
                                </div>

                            </div>

                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Description</label>
                                <div class="col-sm-6 align=left">
                                    <textarea placeholder="Description" name="description" class="form-control"></textarea>
                                </div>

                            </div>

                            <div class="form-group row">
                                <label for="owner" class="col-sm-2 col-form-label">Owner</label>
                                <div class="col-sm-6 align=left">
                                    <input type="text" placeholder="Owner" name="owner" class="form-control">
                                </div>

                            </div>

                            <div class="form-group row">
                                <label for="estimated_time" class="col-sm-2 col-form-label">Estimated time</label>
                                <div class="col-sm-6 align=left">
                                    <input type="number" placeholder="Estimated time" name="estimated_time" class="form-control">
                                </div>

                            </div>

                            <div class="row">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Create</b-button>
                                    <b-button type="submit"  class="btn-large-space" :to="{ name: 'ListTask'}">Cancel</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                taskId: this.$route.params.taskId,
                form: {
                    title: "",
                    description: "",
                    owner: "",
                    estimated_time: null
                }
            }
        },
        methods: {
            onSubmit(evt){
                evt.preventDefault()
                const path = `http://localhost:8000/api/v2.0/task/`

                axios.post(path, this.form).then((response) => {
                    this.form.title = response.data.title
                    this.form.description = response.data.description
                    this.form.owner = response.data.owner
                    this.form.estimated_time = response.data.estimated_time
                    alert("Task Updated")
                })
                .catch((error) => {
                    console.log('error')
                })
                
            }

        }

    }
</script>

<style lang="css" scope>

</style>