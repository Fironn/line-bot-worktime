import $ from 'jquery';
$.ajax({
  type: 'GET',
  url: 'https://wakatime.com/share/@2fce9297-5ba7-422a-aa89-cbaacd4b2508/78e3bc08-4b8a-4833-ba6f-53daeafd4a7f.json',
  dataType: 'jsonp',
  success: function(response) {
    console.log(response.data);
  },
});