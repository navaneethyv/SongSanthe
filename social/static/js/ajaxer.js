$(document).ready(function() {

        $('#upvote').click( function(){

            

            $.ajax({
              url : '/upload/upvote/'+$('#upvote').attr('name'),
              success : function  (result) {
                // alert(result.status);
                res = result.status
                // alert(res)
                // alert(typeof(res))
                if (res == "True")
                {
                  cur = $(".vote_count").text()
                  cur = parseInt(cur)
                  cur = cur+1;
                  $(".vote_count").text(cur)
                  $('#upvote').css({"background-color":"#F0F8FF"})

                }
                else if(res == 'False')
                {
                  cur = $(".vote_count").text()
                  cur = parseInt(cur)
                  cur = cur-1;
                  $(".vote_count").text(cur)       
                  $('#upvote').css({"background":"transparent"})
         
                }
                // body...
              } 
            });



        });

        $('#downvote').click( function(){

            $.ajax({
              url : '/upload/downvote/'+$('#downvote').attr('name'),
              // success : 
            });

        });


        $('.follow_action').click(function(){
                if ($(this).text() == "Following")
                    {
                      get_url = "/friends/ajax/unfollow/"+$(this).attr('id')
                    }
                else
                    {
                      get_url = "/friends/ajax/follow/"+$(this).attr('id')
                    }
                    status_id = $(this).attr('id')
                    // alert($(this).text())


                    // Do follow / unfollow
             $.ajax({
               url : get_url,
               success : function  (response) {
                // alert(response.follow_status)
                $('#'+status_id).text(response.follow_status)

               } 
            });

        });

        $('.ajax_request').click( function(){

          $(this).text('following')
          get_url = $(this).data('url')

          $.ajax({
            url: get_url,
            success : function(response){
              // alert('okay')
            }

          });

        });


        $('.ajax_ignore').click( function(){

          $(this).text('ignored')
          get_url = $(this).data('url')

          $.ajax({
            url: get_url,
            success : function(response){
              // alert('okay')
            }

          });

        });




});
