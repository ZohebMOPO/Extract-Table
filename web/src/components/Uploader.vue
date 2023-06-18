<template>
  <form ref="uploadForm" @submit.prevent="submit">
    <input
      type="file"
      ref="uploadFile"
      @change="onUploadFile"
      class="form-control"
    />
    <button @click="startUpload" name="Upload" value="upload">Submit</button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: null,
    };
  },
  methods: {
    onUploadFile() {
      let file = this.$refs.uploadFile.files[0];
      this.formData = new FormData();
      this.formData.append("file", file);
    },
    startUpload() {
      axios({
        url: "http://localhost:8000/process_file",
        method: "POST",
        data: this.formData,
        headers: {
          Accept: "application.json",
          "Content-Type": "mutlipart/form-data",
        },
      }).then((response) => {
        console.log(JSON.stringify(response.data));
      });
    },
  },
};
</script>
