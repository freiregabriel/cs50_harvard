// https://api.ip2country.info/ip?5.6.7.8
$(document).ready(function() {
    let fetch_ip_btn = document.querySelector('#ip_fetch_btn');
    let ip_input = document.querySelector('#ip_input');
    let ip_data_placeholder = document.querySelector('#ipdata_placeholder');
    const ip_url = (ip) => `https://ipapi.co/${ip}/json/`;

    // add events
    fetch_ip_btn.onclick = (e) => {
        let ip = ip_input.value;
        if (!ip) {
            handleError("No IP found");
            return;
        }
        http.get(ip_url(ip)).then((res) => {
            if (!res || !res.city) {
                handleError('No Country found for this IP');
                return;
            }
            M.toast({ html: 'Success!' });
            let html = `<strong>${res.city} - ${res.region} - ${res.country}/${res.country_name} - ${res.continent_code}</strong>`
            $(ip_data_placeholder).html(html);
        }).catch(e => handleError(e))
    }
})