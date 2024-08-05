// components/TodoTable.tsx
'use client'
import React from 'react';

const TodoTable: React.FC = () => {
  const generateTask = () => {
    // Placeholder for external API call to generate a task
    alert('Generate Task button clicked.');
  };

  const deleteTask = () => {
    // Placeholder for external API call to delete a task
    alert('Delete Task button clicked.');
  };

  return (
    <div className="container mx-auto mt-8 p-4 bg-white shadow-md rounded-lg">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">TaskID</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">TaskTitle</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">TaskDescription</th>
            <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          <tr>
            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">1</td>
            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">Sample Task</td>
            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">This is a sample task description.</td>
            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
              <button
                className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                onClick={generateTask}
              >
                Generate
              </button>
              <button
                className="bg-red-600 text-white px-4 py-2 rounded ml-4 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                onClick={deleteTask}
              >
                Delete
              </button>
            </td>
          </tr>
          {/* Additional rows can be added here */}
        </tbody>
      </table>
    </div>
  );
};

export default TodoTable;
