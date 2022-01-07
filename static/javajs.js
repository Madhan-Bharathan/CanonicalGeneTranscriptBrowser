function myalert() {
            alert("Welcome to GeeksforGeeks.\n " +
                "It is the best portal for computer" + 
                         "science enthusiasts!");
        }
    $(document).ready(function() {
       var table = $('#example').DataTable({
         "language": {
                        "processing": '<i class="fa fa-spinner fa-spin" style="font-size:24px;color:rgb(75, 183, 245);"></i>'
                     }
       });
     });
     function hideLoader() {
    $('#loading').hide();
        }

        $('#example').ready(hideLoader);
   
   
        function openFunc(evt, FunctionName) {
          var i, tabcontent, tablinks;
          tabcontent = document.getElementsByClassName("tabcontent");
          for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
          }
          tablinks = document.getElementsByClassName("tablinks");
          for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
          }
          document.getElementById(FunctionName).style.display = "block";
          evt.currentTarget.className += " active";
        }
        
        
            $(document).ready(function() {
            $('#example').DataTable();
        } );
        