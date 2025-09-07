const MakeAjaxCall = async (url, options) => {

  if (options == undefined)
    options = {method: 'GET', mode: 'cors', cache: 'no-cache'};

  const ajax_request = new Request(url, options);
  const ajax_response = await fetch(ajax_request);

  if (ajax_response.ok) {

    const json_data = await ajax_response.json();
    return Promise.resolve(json_data);

  } else {

    return Promise.reject('Ajax call failed:' + url);

  }
}

function PopulateDropDown(element_id, options, selectedOption) {

  const selector = document.getElementById(element_id);

  options.forEach(function (value, i) {
    let option = document.createElement("option");
    option.value = value;
    option.text = value;
    selector.add(option);
    if (value == selectedOption)
      document.getElementById(element_id).selectedIndex = i+1;
  });
}


