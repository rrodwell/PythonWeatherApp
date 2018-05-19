$(document).ready(function() {
    console.log("JS loaded.")

    $('.celsius').on('click', function(){
        console.log("clicked")
        $('.fahrenheit').removeClass('disabled')
        $('.celsius').addClass('disabled')
        var currentTemp = $('.temp').text().trim();
        currentTemp = (currentTemp - 32) * (5 / 9);
        currentTemp = Math.round(currentTemp)
        $('.temp').html("")
        $('.temp').append(currentTemp)
        
        $('.high').each(function(){
            var forecastHigh = $(this).text();
            forecastHigh = (forecastHigh - 32 ) * (5/9);
            forecastHigh = Math.round(forecastHigh)
            $(this).html("")
            $(this).append(forecastHigh)            
        });

        $('.low').each(function () {
            var forecastLow = $(this).text();
            forecastLow = (forecastLow - 32) * (5 / 9);
            forecastLow = Math.round(forecastLow)
            $(this).html("")
            $(this).append(forecastLow)
            
        });
    });

    $('.fahrenheit').on('click', function () {
        console.log("clicked")
        $('.fahrenheit').addClass('disabled')
        $('.celsius').removeClass('disabled')
        var currentTemp = $('.temp').text().trim();
        currentTemp = (currentTemp * (9/5)) + 32;
        currentTemp = Math.round(currentTemp)
        $('.temp').html("")
        $('.temp').append(currentTemp)

        $('.high').each(function () {
            var forecastHigh = $(this).text();
            forecastHigh = (forecastHigh * (9 / 5)) + 32;
            forecastHigh = Math.round(forecastHigh)
            $(this).html("")
            $(this).append(forecastHigh)
        });

        $('.low').each(function () {
            var forecastLow = $(this).text();
            forecastLow = (forecastLow * (9 / 5)) + 32;
            forecastLow = Math.round(forecastLow)
            $(this).html("")
            $(this).append(forecastLow)

        });
    });

})