<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-center">
                <h1>Tasks</h1>
                <div class="col mb-2">
                    <b-button variant="success" :to="{ name:'CreateTask'}">Create task</b-button>
                </div>
                
                <div class="col-md-12">
                    <b-table striped hover :items="tasks" :fields="fields">
                        
                        <template v-slot:cell(action)="data">
                            <b-button class="m-2" size="sm" variant="primary" :to="{ name:'UpdateTask', params:{taskId: data.item.id}}">
                                Update
                            </b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            fields: [
                { key: 'title', label: 'Title' },
                { key: 'description', label: 'description' },
                { key: 'owner', label: 'Owner' },
                { key: 'estimated_time', label: 'Estimated time' },
                { key: 'time_worked', label: 'Time worked' },
                { key: 'time_left', label: 'Time left' },
                { key: 'overtime_worked', label: 'Overtime worked' },
                { key: 'action', label: ''}

            ],
            tasks: []
        }
    },
    methods: {

        getTask () {

            const path = 'http://localhost:8000/api/v2.0/task/'
            axios.get(path).then((response) => {
                this.tasks = response.data
            })
            .catch((error) => {
                console.log('nasser')
            })
        }

    },

    created(){
        this.getTask()
    }
}
</script>

<style lang="css" scoped>
</style>