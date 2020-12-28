<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text">
                <h2>Update Task</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Time worked</label>
                                <div class="col-sm-6 align=left">
                                    <input type="number" placeholder="Time worked" name="time_worked" class="form-control">
                                </div>

                            </div>

                            <div class="row">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Update</b-button>
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
                    time_worked: ""
                }
            }
        },
        methods: {
            onSubmit(evt){
                evt.preventDefault()
                const path = `http://localhost:8000/api/v2.0/task/${this.taskId}/`

                axios.put(path, this.form).then((response) => {
                    this.form.time_worked = response.data.time_worked
                    alert("Task Updated")
                })
                .catch((error) => {
                    console.log('error')
                })
                
            },

            getTask() {
                const path = `http://localhost:8000/api/v2.0/task/${this.taskId}/`

                axios.get(path).then((response) => {
                    this.form.time_worked = response.data.time_worked
                })
                .catch((error) => {
                    console.log('error')
                })
            }
        },
        created() {
            this.getTask()
        }

    }
</script>

<style lang="css" scope>

</style>