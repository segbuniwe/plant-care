import { useState, useEffect } from 'react';
import { useSignupMutation } from './app/apiSlice';
import { useNavigate } from 'react-router-dom';

const SignUpForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [signup, signupResult] = useSignupMutation();
    const navigate = useNavigate();

    useEffect(() => {
        if (signupResult.isSuccess) {
            navigate("/");
        }
    })

    const handleSignUp = (e) => {
        e.preventDefault();
        const body = {
            username: username,
            email: email,
            password: password,
            first_name: firstName,
            last_name: lastName,
        };
        if (password !== confirmPassword) {
            alert("Passwords do not match!")
            return;
        };
        signup(body);
    };

    return (
        <div>
            <h5>Register</h5>
            <div>
                <form onSubmit={(e) => handleSignUp(e)}>
                    <div>
                        <label>First Name</label>
                        <input
                            name='first_name'
                            type='text'
                            value={firstName}
                            onChange={(e) => {setFirstName(e.target.value)}}
                        />
                    </div>
                    <div>
                        <label>Last Name</label>
                        <input
                            name='last_name'
                            type='text'
                            value={lastName}
                            onChange={(e) => {setLastName(e.target.value)}}
                        />
                    </div>
                    <div>
                        <label>Email</label>
                        <input
                            name='email'
                            type='text'
                            value={email}
                            onChange={(e) => {setEmail(e.target.value)}}
                        />
                    </div>
                    <div>
                        <label>Username</label>
                        <input
                            name='username'
                            type='text'
                            value={username}
                            onChange={(e) => {setUsername(e.target.value)}}
                        />
                    </div>
                    <div>
                        <label>Password</label>
                        <input
                            name='password'
                            type='text'
                            value={password}
                            onChange={(e) => {setPassword(e.target.value)}}
                        />
                    </div>
                    <div>
                        <label>Confirm Password</label>
                        <input
                            name='confirm_password'
                            type='text'
                            value={confirmPassword}
                            onChange={(e) => {setConfirmPassword(e.target.value)}}
                        />
                    </div>
                    <div>
                        <button type='submit'>Register</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default SignUpForm;
