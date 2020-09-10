titleOfProgram="Auto-DIG v.0.2"
###########################################
source /${DIR}/ShellScripts/./functionsForZenityScript.sh
eog --fullscreen /${DIR}/ImagesForApp/tempStartupImage.jpg & sleep 3 && pkill eog
# Allows user to choose what type of assessment they want to generate. Uses preset question lists to create assessments.
typeOfGeneration=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=250 \
    --width=200 \
    --list \
    --text '<b> What do you want to do?</b>' \
    --column 'Generate...' \
    "A Flexible Assessment" \
    "A Progress Quiz" \
    "A Single Module" \
    "A MAC 1105 Final Exam" \
)
escape=$?
checkForEscape $escape
#
footnote_right=$(zenity \
    --title="${titleOfProgram[@]}" \
    --entry \
    --text 'What do you want to print on the bottom-right of the page?'
)
escape=$?
checkForEscape $escape
db_name="$(( 1000 + RANDOM % 9000 ))-$(( 1000 + RANDOM % 9000 ))"
footnote_left=$(zenity \
    --title="${titleOfProgram[@]}" \
    --height=100 \
    --width=400 \
    --info \
    --text="You have been assigned ${db_name}. You'll need this to provide students specific feedback."
)
escape=$?
checkForEscape $escape
number_of_versions=$(zenity \
    --title="${titleOfProgram[@]}" \
    --scale \
    --text="How many versions do you want to create?" \
    --value=3 \
    --min-value=1 \
    --max-value=26 \
    --step=1
)
escape=$?
checkForEscape $escape
defineVersionList
###
if [ "$typeOfGeneration" == "A Progress Quiz" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateProgressQuiz.sh
elif [ "$typeOfGeneration" == "A Single Module" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateSingleModule.sh
elif [ "$typeOfGeneration" == "A MAC 1105 Final Exam" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateMAC1105FinalExam.sh
elif [ "$typeOfGeneration" == "A Flexible Assessment" ]; then
    source /${DIR}/ShellScripts/Types_of_Generation/./generateFlexibleAssessment.sh
fi
(
# Clears old keys and pdfs
rm -rf /${DIR}/Keys/*
rm -rf /${DIR}/BuildExams/*
StartTime=$( date +'%s' )
number_of_questions=${#question_list[@]}
question_step=$(( 100 / (number_of_questions*number_of_versions) ))
counter=0
END=${#list_of_assessment_titles[@]}
while true
do
    mkdir /$DIR/CompleteExam/"$exam_display_name"
    mkdir /$DIR/CompleteExam/"$exam_display_name"/PDFs
    mkdir /$DIR/CompleteExam/"$exam_display_name"/Keys
    for ((index=0;index<END;index++))
    do
        title=${list_of_assessment_titles[index]}
        question_list_name=$title
        #question_list_name="$title$index"
        #question_list="${!question_list_name}"
        for version in ${version_list[@]}
        do
            full_db_name="$db_name-Ver$version"
            echo "$counter" ; sleep 0
            counter=$(( counter+question_step ))
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Exam File" $title "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Create Key File" $title "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            for question in ${question_list[@]}
            do
                echo "#Running ${question} for version ${version}."
                run_save_metadata="/$DIR/PythonScripts/ScriptsForDatabases/saveMetadataToNewDatabase.py"
                python3 $run_save_metadata $DIR $question "$full_db_name" $title
                return_error=1
                error_counter=0
                while [ $return_error -ne 0 ]
                do
                    if [ $error_counter -ne 0 ]; then
                        echo "#An error occured while running ${question} for version ${version}. Don't worry - we will continue to try again. Attempt: ${error_counter}"
                    fi
                    run_return_key_value_from_db="/$DIR/PythonScripts/ScriptsForDatabases/return_key_value_from_db.py"
                    code_folder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Folder" )
                    code_subfolder=$( python3 $run_return_key_value_from_db $DIR $full_db_name $question_list_name $question "Subfolder" )
                    question_py="/$DIR/Code/$code_folder/$code_subfolder/$question.py"
                    # Runs python code to generate question data
                    python3 $question_py $DIR $full_db_name $question_list_name $version
                    # Question data has now been saved with the metadata.
                    return_error=$?
                    error_counter=$(( error_counter+1 ))
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to exam" $DIR $title $full_db_name $question_list_name $question $version
                python3 /$DIR/PythonScripts/ScriptsForPDFs/printQuestions.py "Print questions to key" $DIR $title $full_db_name $question_list_name $question $version
                counter=$(( counter+question_step ))
                done
            done
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Exam File" $title "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            python3 /$DIR/PythonScripts/ScriptsForPDFs/createFiles.py "Finish Key File" $title "$exam_display_name" "$footnote_left" "$footnote_right" $version $DIR
            cd /$DIR/BuildExams/
            pdflatex -file-line-error -halt-on-error ${title}${version}.tex
            cp ${title}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/PDFs
            cd /$DIR/Keys/
            pdflatex -file-line-error -halt-on-error key${title}${version}.tex
            cp key${title}${version}.pdf /$DIR/CompleteExam/"$exam_display_name"/Keys
            cd /$DIR/ShellScripts/
        done
    done
    break
done
xdg-open /${DIR}/CompleteExam/"$exam_display_name"
EndTime=$( date +'%s' )
currentDayTime=$( date +'%H:%M on %m/%d/%Y' )
TotalRunTimeSeconds=$(( EndTime - StartTime ))
RunTimeMinutes=$(( (EndTime - StartTime) / 60 ))
RunTimeSecondsRemainder=$(( TotalRunTimeSeconds - (RunTimeMinutes * 60) ))
echo "100"
echo "# Auto-DIG has finished running at ${currentDayTime}. It took $RunTimeMinutes minutes and $RunTimeSecondsRemainder seconds. Not bad!"
) |
zenity --progress \
  --title="${titleOfProgram[@]}" \
  --text="Initializing parameters..." \
  --percentage=0 \
  --width=350 \
  --pulsate
