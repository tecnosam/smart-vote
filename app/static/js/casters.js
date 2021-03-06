const cast_poll = (poll) => `

    <div>
        <div class = "card">
        <div class="card-header">
            <h6 class="text-uppercase text-center mb-0">${poll.tag}</h6>

            <div class="text-center mb-0" style="text-align: center; margin-top: 2%; margin-bottom: 2%">
                <small>${poll.desc}</small>
            </div>

            <h6 class="text-center text-blue mb-0">
                <a data-toggle="modal" data-target="#edit-poll-${poll.id}" href="javascript:void(0)">
                    edit Poll
                </a>
            </h6>
            <h6 class="text-center text-blue mb-0">
                <a data-toggle="modal" data-target="#add-option-${poll.id}" href="javascript:void(0)">
                    add new option
                </a>
            </h6>
        </div>
        <div class="card-body">                           
            <table class="table table-striped table-hover card-text">
                <thead>
                    <tr>
                    <th>Tag</th>
                    <th>desc</th>
                    </tr>
                </thead>
                <tbody id="poll-${poll.id}-options">
                    ${ poll.options.map( o => cast_option( o ) ).join("") }
                </tbody>
            </table>
        </div>
        </div>
    </div>

    <div id="edit-poll-${poll.id}" tabindex="-1" role="dialog" aria-labelledby="editPosModal" class="modal fade text-left" style="display: none;">
        <div role="document" class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">

            <h4  class="modal-title">
                    Edit ${poll.tag}
                    <a class="mb-0 f-10" style="font-size: 12pt; color: red;" href="javascript:delete_poll( "${poll.id}" )">DELETE</a>
            </h4>

            <button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">×</span></button>
            </div>
            <form method="POST" action="javascript:edit_poll(${poll.id})">
                <div class="modal-body">
                    <div class="form-group">
                        <label>Tag</label>
                        <input type="text" name="tag" id="edit-poll-${poll.id}-tag" value="${poll.tag}" placeholder="Enter Poll tag" required class="form-control">
                    </div>

                    <div class="form-group">
                        <label>Description</label>
                        <input type="text" name="desc" id="edit-poll-${poll.id}-desc" value="${poll.desc}" placeholder="Enter Poll description" class="form-control">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" data-dismiss="modal" class="btn btn-secondary">Close</button>
                    <input type="submit" class="btn btn-primary asyncTrigger" value="Save changes">
                </div>
            </form>
        </div>
        </div>
    </div>

    <!-- add new option -->
    <div id="add-option-${poll.id}" tabindex="-1" role="dialog" aria-labelledby="addOptionModal" class="modal fade text-left" style="display: none;">
        <div role="document" class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <h4 class="modal-title">Add an option ${poll.tag}</h4>
            <button type="button" data-dismiss="modal" aria-label="Close" class="close"><span aria-hidden="true">×</span></button>
            </div>
            <form method="POST" action="javascript:add_option( ${poll.id} )" >
                <div class="modal-body">
                    <div class="form-group">
                        <label>Tag</label>
                        <input type="text" name="tag" id="add-option-${poll.id}-tag" placeholder="add a tag to your option" required class="form-control">
                    </div>
                    <div class="form-group">
                        <label> Add a description (optional) </label>
                        <input type="text" name="desc" id="add-option-${poll.id}-desc" placeholder="Add a description" class="form-control">
                    </div>

                </div>
                <div class="modal-footer">

                    <button type="button" data-dismiss="modal" class="btn btn-secondary">Close</button>

                    <input type="submit" class="btn btn-primary" value="Save changes">

                </div>

            </form>
        </div>
        </div>
    </div>

`

const cast_option = (option) => `

    <tr id="option-${option.id}" >
        <td>${option.tag}</td>
        <td>${option.desc}</td>

        <td onclick="delete_option(${option.id})">
            <a class="text-red text-uppercase" href="javascript:void(0)">
                delete
            </a>
        </td>

    </tr>

`

const cast_meeting = ( meeting ) => `

`