
$(document).on('ready', function(){

	teste()
		});
	function teste(){

	$.ajax({

		type:"GET",
		contentType:"application/json; charset=utf-8",
		dateType:"jason",
		url:"/portabilidade/teste/",
		success:function(response){

				var trHTML = '';
				$.each(response, function(i,fields){

					trHTML +=  
					'<tr><td  class="text-align-center">' + response[i].fields.numero + 
					'</td><td class="text-align-center">' + response[i].fields.operadora + 
					'</td><td class="text-align-center">' + response[i].fields.tipo + 
					'</td><td class="text-align-center">' + response[i].fields.hora + 
					'</td><td class="text-align-center">' + response[i].fields.valor + 
					'</td></tr>';
				});
					$('#tabela').append(trHTML);
					
				// console.log(response);
				 
					//setTimeout('teste()', 10000);
					// setInterval( function () {
    	// 				$('td').text('atualizando...');
    	// 				trHTML += trHTML;
					// }, 10000 );

	
		}
		
	});
	
	}