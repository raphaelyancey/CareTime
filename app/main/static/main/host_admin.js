$(document).ready(function() {

    var NOW = {
        hours: (new Date()).getHours(),
        minutes: (new Date()).getMinutes()
    };

    console.log('••• NOW', NOW)

    var utils = {
        zero_pad: function(input) {
            if(input < 10 && input > 0) return '0'+input;
            else if(input == 0) return '00';
            else return input+'';
        },
        format: function(input) {
            return this.zero_pad(parseInt(input));
        }
    };
    
    new Vue({
        delimiters: ['[[', ']]'],
        el: '#pickup-form',
        data: {
            scheduled_hours: utils.format(NOW.hours),
            scheduled_minutes: utils.format(NOW.minutes),
        },
        computed: {
            scheduled_time: function() {
                var u = utils;
                return u.format(this.scheduled_hours)+':'+u.format(this.scheduled_minutes);
            }
        },
        methods: {
            increase_hour: function() {
                h = parseInt(this.scheduled_hours);
                u = utils;
                this.scheduled_hours = (h+1 >= 24) ? 0 : h+1;
                this.scheduled_hours = u.format(this.scheduled_hours);
            },
            decrease_hour: function() {
                h = parseInt(this.scheduled_hours);
                u = utils;
                this.scheduled_hours = (h-1 < 0 ) ? 23 : h-1;
                this.scheduled_hours = u.format(this.scheduled_hours);
            },
            increase_minutes: function() {

                h = parseInt(this.scheduled_minutes);
                u = utils;

                if(h >= 0 && h < 15)
                    this.scheduled_minutes = 15;
                else if(h >= 15 && h < 30)
                    this.scheduled_minutes = 30;
                else if(h >= 30 && h < 45)
                    this.scheduled_minutes = 45;
                else if(h >= 45)
                    this.scheduled_minutes = 0;

                this.scheduled_minutes = u.format(this.scheduled_minutes);
            },
            decrease_minutes: function() {

                h = parseInt(this.scheduled_minutes);
                u = utils;

                if(h > 0 && h <= 15)
                    this.scheduled_minutes = 0;
                else if(h > 15 && h <= 30)
                    this.scheduled_minutes = 15;
                else if(h > 30 && h <= 45)
                    this.scheduled_minutes = 30;
                else if(h > 45 || h == 0)
                    this.scheduled_minutes = 45;

                this.scheduled_minutes = u.format(this.scheduled_minutes);
            },
            format_hour: function() {
                var u = utils;
                this.scheduled_hours = u.format(this.scheduled_hours);
            },
            format_minutes: function() {
                var u = utils;
                this.scheduled_minutes = u.format(this.scheduled_minutes);
            }
        }
    })
});