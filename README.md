# ds_algo from LEETCODE




<div class="collapse" id="diet_gym" data-collapse-group="collapse-group-2">
                  <div class="well">
                    <div class="row">
                        {% for data_root in datas[key] %}
                        <div class="col-md-3">
                            <button class="title-class" type="button" data-toggle="collapse" data-target="#{{data_root}}" aria-expanded="false" aria-controls="collapseExample">
                              {{data_root}}
                            </button>
                        </div>
                        {% endfor %}
                     </div>

                      {% for gym_data_root in datas[key] %}
                      <div class="row" style="justify-content: center">
                         <div class="collapse" id="{{gym_data_root}}" data-collapse-group="collapse-group">
                            <div class="well content-wrapper">
                                {% for real_content in gym_content_keys[gym_data_root] %}
                                    {% if gym_data_root == 'daily-workouts' %}
                                        {% for i in range(15) %}

                                            <div class="col-md-4 ">
<!--                                                <div class="img-container">-->
                                                    <img class="make_bigger workout-img" src="/{{gym_content[gym_data_root][real_content]}}">
<!--                                                </div>-->
                                            </div>
                                        {% endfor %}
                                    {% else %}
                                        {% for i in range(15) %}
<!--                                        <div class="well content-wrapper">-->
                                            <div class="col-md-4">
                                                <video class="workout-video" width="320" height="240" controls>
                                                  <source src="/{{gym_content[gym_data_root][real_content]}}" type="video/mp4">
            <!--                                      <source src="movie.ogg" type="video/ogg">-->
                                                    Your browser does not support the video tag.
                                                </video>
                                            </div>
<!--                                        </div>-->
                                        {% endfor %}
                                    {% endif %}
                                {% endfor %}
                            </div>
                        </div>
                      </div>
                      {% endfor %}
                  </div>
            </div>